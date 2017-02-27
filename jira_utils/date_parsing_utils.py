from datetime import datetime

DATE_FORMAT_1 = '%m/%d/%Y'              # 02/25/2017 : 25 Feb 2017
DATE_FORMAT_2 = '%Y-%m-%d'              # 2017-02-15 : 15 Feb 2017
DATE_FORMAT_3 = '%m-%d-%y'              # 02-10-17   : 10 Feb 2017

DATE_FORMAT_LIST = {DATE_FORMAT_1, DATE_FORMAT_2, DATE_FORMAT_3}

DATETIME_FORMAT_1 = '%d-%m-%y %H:%M'            # 10-03-17 18:00                : 10 Mar 2017 18:00
DATETIME_FORMAT_2 = '%Y-%m-%dT%H:%M:%S.%f%z'    # 2017-03-01T19:00:00.000-0500  : 01 Mar 2017 19:00 Eastern

def get_target_date(target_date_str : str, key : str) -> datetime :
    if target_date_str :
        parsing_success_flag = False
        for date_format in DATE_FORMAT_LIST :
            try :
                target_date = datetime.strptime(target_date_str, date_format)
                parsing_success_flag = True
            except ValueError :
                parsing_success_flag = False
                print('Using alternate Date format: {0} for Key={1}'.format(date_format, key))

            if parsing_success_flag :
              break

        if parsing_success_flag :
            return target_date
        else :
            print('Unable to parse Target Date : ', target_date_str, ' for Key : ', key)
            return None
    else :
        return None

def get_production_drop_date (production_drop_date_str : str, key : str) -> datetime :
    if production_drop_date_str :
        prod_drop_date = datetime.strptime(production_drop_date_str, DATETIME_FORMAT_1)
        return prod_drop_date
    else :
        return None
