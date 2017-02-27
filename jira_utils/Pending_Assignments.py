import csv
from datetime import datetime
from pprint import pprint

# import funtions from date_parsing_utils.py
import date_parsing_utils as my_module

DESIRED_DAYS_GAP = 14

PENDING_ASSIGNMENTS_JIRA_FILE = '..\Data\Pending_Assignments.csv'

with open(PENDING_ASSIGNMENTS_JIRA_FILE, 'r') as csvfile :
    csv_reader = csv.reader(csvfile)
    # sniff into 10KB of the file to check its dialect
    dialect = csv.Sniffer().sniff( csvfile.read( 10*1024 ) )
    csvfile.seek(0)

    # read csv file according to dialect
    csv_reader = csv.reader( csvfile, dialect )

    # read header
    header_row = next(csv_reader)
    header_tup = tuple(header_row)
    pprint(header_tup)

    key_index               = header_tup.index('Key')
    target_date_index       = header_tup.index('Target Date')
    prod_drop_date_index    = header_tup.index('Production Drop Date')
    assignee_index          = header_tup.index('Assignee')
    status_index            = header_tup.index('Status')

    print('Key @ {0}, Target Date @ {1}, Production Drop Date @ {2}'.format(key_index, target_date_index, prod_drop_date_index))

    key = ''
    target_date = datetime.today()
    prod_drop_date = datetime.today()

    missing_prod_date_list = []
    missing_target_date_list = []
    prod_drop_date_adjust_list = []

    while True :
        try :
            data_row = next(csv_reader)
        except StopIteration :
            break
        
        data_tup = tuple(data_row)
        key = data_tup[key_index]
        
        prod_drop_dt_str = data_tup[prod_drop_date_index]
        prod_drop_date = my_module.get_production_drop_date(prod_drop_dt_str, key)

        if prod_drop_date :
            target_dt_str = data_tup[target_date_index]
            target_date = my_module.get_target_date(target_dt_str, key)

            if target_date :
                timedelta = prod_drop_date - target_date
                days_gap = timedelta.days
            
                if (days_gap < DESIRED_DAYS_GAP) :
                    prod_drop_date_adjust_list.append(key)
            else :
                missing_target_date_list.append(key)
                
        elif prod_drop_date is None :
            missing_prod_date_list.append(key)

    print('Adjust Production Drop Date for:')
    pprint(prod_drop_date_adjust_list)

    print('---------------------------------------------')
    print('---------------------------------------------')
    print('---------------------------------------------')

    print('Missing Target Date :')
    pprint(missing_target_date_list)

    print('=============================================')
    print('=============================================')
    print('=============================================')

    print('Missing Production Drop Date :')
    pprint(missing_prod_date_list)
    
        
