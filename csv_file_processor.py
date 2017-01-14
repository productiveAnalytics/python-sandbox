import os
from pathlib import Path
import csv

cwd = os.getcwd()
print('Current working directory = ', cwd)

# Format : State ID, State, Capital, Polulation, University Town (Y/N), Business Center (Y/N), Timezone
columns_list = ['State ID', 'State', 'Capital', 'Polulation', 'University Town', 'Business Center', 'Timezone']
state_capitals = { 'NY' : ['New York', 'Albany', 150500, True, False, 'ET'],
                   'NC' : ['North Carolina', 'Raleigh', 1000020, False, True, 'ET'],
                   'OH' : ['Ohio', 'Columbus', 400000, False, True, 'ET'],
                   'WI' : ['Wisconsin', 'Madison', 230000, True, False, 'CT'],
                   'IN' : ['Indian', 'Indianapolis', 550000, False, True, 'CT'],
                   'IA' : ['Iowa', 'Des Moines', 250000, False, True, 'CT'],
                   'CO' : ['Colorado', 'Denver', 1500000, False, True, 'MT'],
                   'UT' : ['Utah', 'Salt Lake City', 1200100, True, True, 'MT'],
                   'TX' : ['Texas', 'Austin', 1800500, True, True, 'MT'],
                   'CA' : ['California', 'Sacramento', 1705500, True, False, 'PT'],
                   'WA' : ['Washington', 'Seatle', 2000000, True, True, 'PT'] 
                }

def create_new_or_open_existig_csv(filename: str) -> 'fhandle' :
    
    csv_abs_path = Path('./Data/'+filename)
    print('CSV File = '+ str(csv_abs_path))
    if not csv_abs_path.exists() :
        with open(csv_abs_path, 'w') as fhandle:
        
            column_line = '' 
        
            # insert the column headings
            column_line = ','.join(columns_list)
            #print('DEBUG--', column_line)
            print(column_line, file = fhandle)
        
            # insert the data
            for (sid, cap) in state_capitals.items() :
                cap.insert(0, sid)
                column_line = ','.join(str(x) for x in cap)
                #print('DEBUG--', column_line)
                print(column_line, file = fhandle)
                
        print('>>>Created new CSV file {0}'.format(csv_abs_path))    
    else :
        print('>>>Using existing CSV file: {0}'.format(csv_abs_path))
        
    fhandle = open(csv_abs_path, 'r')
    return fhandle

print()
print()
print('********* Printing CSV file as List *********')
with create_new_or_open_existig_csv('state_capitals.csv') as csvfile :
    for line_list in csv.reader(csvfile) :
        print(line_list)

print()
print()
print('********* Printing CSV file as Dictionary *********')
with create_new_or_open_existig_csv('state_capitals.csv') as csvfile :
    for line_dict in csv.DictReader(csvfile) :
        print(line_dict)
