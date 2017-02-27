import subprocess
import shlex

import json

from pprint import pprint

AUTH_TOKEN = 'bGNoYXdhdGhlOlBhNTV3b3JkMUAz'
command_template = 'curl -D- -X GET -H "Authorization: Basic AUTH_TOKEN" "Content-Type: application/json" https://v3.vitechinc.com/jira/rest/api/2/issue/JIRA_KEY?expand=names&fields=status,customfield_10409,customfield_10304,customfield_14800'

def retrieve_JIRA_fields (key: str)  -> dict :
    command_line = command_template.replace('AUTH_TOKEN', AUTH_TOKEN)
    command_line = command_line.replace('JIRA_KEY', key)

    print('Command: ', command_line)
    
    args = shlex.split(command_line)
##    print(args)

    # Implementation 1
    # cURL_proc = subprocess.Popen(command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Implementation 2
    cURL_proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = cURL_proc.communicate()

    response = out.decode("utf-8")

    start_of_json = response.find("{")
    end_of_json = response.rfind("}")
##    print('Start={0} & End={1}'.format(start_of_json, end_of_json))

    json_response = response[start_of_json : end_of_json+1]
##    print(json_response)

    json_obj = json.loads(json_response)

    names_str = json_obj['names']
    names_dict = dict(names_str)
    #pprint(names_dict)

    fields_str = json_obj['fields']
    fields_dict = dict(fields_str)
    #pprint(fields_dict)

    output_dict = {}

    for (k,v) in names_dict.items() :
        if v == 'Status' :
            status_str = fields_dict['status']
            status_dict = dict(status_str)
            status_name = status_dict['name']
            attr_value = status_name
        else :
            attr_value = fields_dict[k]
            
        print('{0} = {1} '.format(v, attr_value))
        output_dict[v] = attr_value

    return output_dict
## end of retrieve_JIRA_fields()

if __name__ == '__main__' :
    test_dict = retrieve_JIRA_fields('ETF-14700')
    pprint(test_dict)

    

