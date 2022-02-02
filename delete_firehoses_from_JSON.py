#!/usr/bin/env python3

import json
import subprocess
import boto3

MODULE_NAME:str='con-common'
NEED_S3_CLEANUP:bool = True
S3_BUCKET_BY_ZONE:dict = {False: "laap-ue1-gen-landing-sbx", True: "laap-ue1-gen-conformance-sbx"}

# pull the JSON from Lambda's SSM parameter
JSON_FROM_LAMBDA:str='{"ads_rtcrd__rate_card_type":"laap-kdf-ue1-datasink-datasync03-ads_rtcrd__rate_card_type-sbx","ads_common__division":"laap-kdf-ue1-datasink-datasync03-ads_common__division-sbx","ads_invntry__feat_cat_typ":"laap-kdf-ue1-datasink-datasync03-ads_invntry__feat_cat_typ-sbx","conformance_target_concommon__invntry_avail_spot_ty":"laap-kdf-ue1-datasink-datasync03--1460770584-sbx","ads_rtcrd__flight_quarter":"laap-kdf-ue1-datasink-datasync03-ads_rtcrd__flight_quarter-sbx","ads_common__outlet_group":"laap-kdf-ue1-datasink-datasync03-ads_common__outlet_group-sbx","ads_invntry__inventory_type":"laap-kdf-ue1-datasink-datasync03-ads_invntry__inventory_type-sbx","ads_rtcrd__rttn_prd_rls_src_typ":"laap-kdf-ue1-datasink-datasync03-635707822-sbx","ads_prpsl__flight_week":"laap-kdf-ue1-datasink-datasync03-ads_prpsl__flight_week-sbx","ads_rtcrd__pkg_sllng_rttn_typ":"laap-kdf-ue1-datasink-datasync03-2008940914-sbx","conformance_target_concommon__demo_cmpst_asgmnt":"laap-kdf-ue1-datasink-datasync03--1553493079-sbx","ads_rtcrd__pkg_sr_cnstrnt_typ":"laap-kdf-ue1-datasink-datasync03--463522609-sbx","ads_prpsl__flight_day":"laap-kdf-ue1-datasink-datasync03-ads_prpsl__flight_day-sbx","conformance_target_concommon__dlvry_stream":"laap-kdf-ue1-datasink-datasync03--2004846701-sbx","ads_common__region":"laap-kdf-ue1-datasink-datasync03-ads_common__region-sbx","conformance_target_concommon__flght_rng":"laap-kdf-ue1-datasink-datasync03--1679082512-sbx","ads_rtcrd__delivery_metric_provider":"laap-kdf-ue1-datasink-datasync03--47862727-sbx","conformance_target_concommon__outlt_grp_outlt":"laap-kdf-ue1-datasink-datasync03--2127115030-sbx","conformance_target_concommon__lkup_ref":"laap-kdf-ue1-datasink-datasync03--468267017-sbx","ads_invntry__exclsvty_typ":"laap-kdf-ue1-datasink-datasync03-ads_invntry__exclsvty_typ-sbx","ads_rtcrd__demographic":"laap-kdf-ue1-datasink-datasync03-ads_rtcrd__demographic-sbx","conformance_target_concommon__demo":"laap-kdf-ue1-datasink-datasync03--1827817684-sbx","ads_common__app_rgstry":"laap-kdf-ue1-datasink-datasync03-ads_common__app_rgstry-sbx","conformance_target_concommon__cal_dt":"laap-kdf-ue1-datasink-datasync03-76464554-sbx","ads_prpsl__flight_month":"laap-kdf-ue1-datasink-datasync03-ads_prpsl__flight_month-sbx","conformance_target_concommon__outlt":"laap-kdf-ue1-datasink-datasync03--817131219-sbx","ads_rtcrd__audience_unit_of_measure":"laap-kdf-ue1-datasink-datasync03--1096980678-sbx","ads_rtcrd__metric_source_demographic":"laap-kdf-ue1-datasink-datasync03--249214452-sbx","ads_invntry__unit_length":"laap-kdf-ue1-datasink-datasync03-ads_invntry__unit_length-sbx","ads_common__outlet_extension":"laap-kdf-ue1-datasink-datasync03-1407738951-sbx","ads_prpsl__flight_quarter":"laap-kdf-ue1-datasink-datasync03-ads_prpsl__flight_quarter-sbx","ads_common__outlet_channel":"laap-kdf-ue1-datasink-datasync03-ads_common__outlet_channel-sbx","ads_invntry__feat_typ":"laap-kdf-ue1-datasink-datasync03-ads_invntry__feat_typ-sbx","conformance_target_concommon__feat_ty":"laap-kdf-ue1-datasink-datasync03-842923721-sbx","conformance_target_concommon__src_sys_ref":"laap-kdf-ue1-datasink-datasync03--1763398819-sbx","ads_prpsl__reference":"laap-kdf-ue1-datasink-datasync03-ads_prpsl__reference-sbx","conformance_target_concommon__crncy_exchg_rt":"laap-kdf-ue1-datasink-datasync03-878590437-sbx"}'

topics_2_firehose_dict:dict = json.loads(JSON_FROM_LAMBDA)

kdf_cli = boto3.client('firehose')
s3_resource = boto3.resource('s3')

LANDING_S3_BUCKET = s3_resource.Bucket(S3_BUCKET_BY_ZONE[False])
assert LANDING_S3_BUCKET != None
CONFORMANCE_S3_BUCKET = s3_resource.Bucket(S3_BUCKET_BY_ZONE[True])
assert CONFORMANCE_S3_BUCKET != None
print(f'\nLanding bucket={LANDING_S3_BUCKET} \Conformance bucket={CONFORMANCE_S3_BUCKET}')

topic_kdf_pair:dict=dict()

errored_kdfs_landing:list=list()
errored_kdfs_conformance:list=list()

effective_bucket = None
s3_folder_path:str = ''
s3_uri:str = ''

for topic_name in topics_2_firehose_dict.keys():
    kdf_name = topics_2_firehose_dict[topic_name]
    print(f'Topic={topic_name} Firehose={kdf_name}')

    is_conformed:bool = True if ('conformance_' in topic_name) else False

    if is_conformed:
        effective_bucket = LANDING_S3_BUCKET
        s3_topic_folder_path = f'landing-topics/{topic_name}/'
    else:
        effective_bucket = CONFORMANCE_S3_BUCKET
        s3_topic_folder_path = f'conformance-topics/{MODULE_NAME}/{topic_name}/'

    s3_uri = "s3://{s3_bucekt}/{s3_foler}".format(s3_bucekt=effective_bucket.name, s3_foler=s3_topic_folder_path)
    try:
        del_kdf_response = kdf_cli.delete_delivery_stream(
            DeliveryStreamName=kdf_name,
            AllowForceDelete=True
        )
        print(f'Deleted firehose: {kdf_name}')
    except Exception as err:
        # print("ERROR {0}".format(err))
        topic_kdf_pair = {topic_name: {"kdf": kdf_name, "s3_folder": s3_topic_folder_path, "s3_uri": s3_uri}}
        if is_conformed:
            errored_kdfs_conformance.append(topic_kdf_pair)
        else:
            errored_kdfs_landing.append(topic_kdf_pair)
        
    if NEED_S3_CLEANUP:
        try:
            # delete_s3_folder_response = effective_bucket.delete_objects(
            #     Delete={
            #         'Objects': [
            #             {
            #                 'Key': s3_topic_folder_path
            #             },
            #         ],
            #         'Quiet': False
            #     }
            # )

            # deleted_s3_key:str = delete_s3_folder_response['Deleted'][0]['Key']
            # print(f'Deleted s3 path: {deleted_s3_key}')
            effective_bucket.objects.filter(Prefix=s3_topic_folder_path).delete()
            print(f'Deleted s3 topics folder: {s3_topic_folder_path}')
        except Exception as s3_ex:
            print("S3_ERROR {0}".format(s3_ex))
    else:
        print(f'INFO: Associated S3 folder for Firehose {kdf_name}: {s3_topic_folder_path}')


def cleanup(zone:str, errored_list:list) -> None:
    print("\n\n ERROR: {zone} {topics_err_count} topic/firehose(s)".format(zone=zone, topics_err_count=len(errored_list)))
    for zone_aware_topic_firehose in errored_list:
        print(zone_aware_topic_firehose)
        topic_name = next(iter(zone_aware_topic_firehose.keys()))
        s3_uri_to_delete:str = zone_aware_topic_firehose[topic_name]['s3_uri']
        p_result = subprocess.run(['aws', 's3', 'rm', s3_uri_to_delete, '--recursive'], capture_output=True, text=True)
        # print("stdout:", p_result.stdout)
        # print("stderr:", p_result.stderr)

# deep clean-up
cleanup(zone='Landing', errored_list=errored_kdfs_landing)
cleanup(zone='Conformance', errored_list=errored_kdfs_conformance)