import csv
from datetime import datetime
from pprint import pprint

# import funtions from date_parsing_utils.py
import date_parsing_utils as date_util

# import funtions from jira_utils.py
import jira_utils

DESIRED_DAYS_GAP = 14

PENDING_PRODUCT_JIRA_FILE = '..\Data\Pending_pe_pi.csv'

with open(PENDING_PRODUCT_JIRA_FILE, 'r') as csvfile :
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
    links_index             = header_tup.index('Linked Issues')     # fields=issuelinks
    target_date_index       = header_tup.index('Target Date')
    assignee_index          = header_tup.index('Assignee')
    status_index            = header_tup.index('Status')

    print('Key @ {0}, Target Date @ {1}, Assignee @ {2} and Issue'.format(key_index, target_date_index, assignee_index))

    key = ''
    target_date = datetime.today()
    prod_drop_date = datetime.today()

    missing_target_date_list = []
    target_date_adjust_list = []

    while True :
        try :
            data_row = next(csv_reader)
        except StopIteration :
            break

        data_tup = tuple(data_row)
        key = data_tup[key_index]

        linked_items_str = data_tup[links_index]
        linked_items_list = linked_items_str.split(',')
        pprint(linked_items_list)

        target_date_str = data_tup[target_date_index]
        target_date = date_util.get_target_date(target_date_str, key)
        if not target_date :
            missing_target_date_list.append(key)
        else :
            for linked_item in linked_items_list :
                linked_item_key = linked_item.strip(' ')
                linked_item_dict = jira_utils.retrieve_JIRA_fields(linked_item_key)

                linked_item_status = linked_item_dict['Status']

                if linked_item_status == 'Closed' :
                    continue

                linked_item_Target_Date_str = linked_item_dict['Target Date']
                linked_item_Target_Date = date_util.get_target_date(linked_item_Target_Date_str, linked_item_key)

                if not linked_item_Target_Date :
                    continue

                # if product item has higher Target Date than its linked client item Target Date
                if target_date > linked_item_Target_Date :
                    client_target_date_repr    = datetime.strftime(linked_item_Target_Date, date_util.DATE_FORMAT_1)
                    product_target_date_repr   = datetime.strftime(target_date, date_util.DATE_FORMAT_1)
                    print('Target Date {0} for product item: {1} is AFTER Target Date {2} for client item: {3}'.format(product_target_date_repr, key, client_target_date_repr, linked_item_key))
                    target_date_adjust_list.append('Key='+ linked_item_key +' Status='+ linked_item_status +' Target Date: '+ client_target_date_repr +' < '+ '(Product) Target Date: '+ product_target_date_repr)

    
    print('---------------------------------------------')
    print('---------------------------------------------')
    print('---------------------------------------------')

    print('Missing Target Date :')
    pprint(missing_target_date_list)

    print('=============================================')
    print('=============================================')
    print('=============================================')

    print('Adjust client Target Date for :')
    pprint(target_date_adjust_list)
