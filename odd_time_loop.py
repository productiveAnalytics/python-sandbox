from datetime import datetime

import time
import random

max_loop_count = 5

odd = []

i=1
while i < 60:
    if (i % 2 == 1) :
        odd.append(i)
    
    i=i+1

# print the contents of the list
#print('Odd minutes = {}'.format(odd))

for i in range(max_loop_count):
    right_now_minute = datetime.today().minute
    
    if right_now_minute in odd:
        print('{0}: This is odd time'.format(i))
    else:
        print('{0}: Not an odd time'.format(i))

    # skip sleep for last iteration
    if i < (max_loop_count-1) :
        sleep_time = random.randint(1,60);
        print('{0}: Sleeping for {1} seconds...'.format(i, sleep_time))
        time.sleep(sleep_time)
    
