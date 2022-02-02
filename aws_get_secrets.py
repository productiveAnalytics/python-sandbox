#!/usr/bin/env python3

from pprint import pprint
import boto3
import base64
from botocore.exceptions import ClientError
import json

def get_secret(secret_name:str, region_name:str='us-east-1') -> str :
    """
    Method to retrieve secrets from AWS Secret Manager. 

    Example to retrieve secrets:
    command = ['cp', 'cdp-airflow.cfg', '/home/airflow/cdp-airflow.cfg']

    Returns retrieved secrets as plain text.

    """
    #logging.info('Fetching secret for %s in region: %s', secret_name, region_name)

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            print('Found unencoded secret')
            secret_text = get_secret_value_response['SecretString']
            return secret_text
        else:
            print('Found base64 encoded secret')
            secret_decoded_binary = base64.b64decode(get_secret_value_response['SecretBinary'])
            return secret_decoded_binary


if __name__ == '__main__':
    # my_secret_key:str = 'lineardp/dev/airflow/connections/oracle/edw'

    # ARN: arn:aws:secretsmanager:us-east-1:887847050650:secret:laap-sec-ue1-mstr-encryptorcl-sandbox-PLyntU
    my_secret_key:str = 'laap-sec-ue1-mstr-encryptorcl-sandbox'
    my_secret_value:str = get_secret(secret_name=my_secret_key)
    print('Secret found: Key: {} = Value: {}'.format(my_secret_key, my_secret_value))

    my_dict = json.loads(my_secret_value)
    for key in my_dict.keys():
        print("key: ", key, " value:", my_dict[key])