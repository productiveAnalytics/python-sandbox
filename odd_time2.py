from datetime import datetime

odd = []

i=1
while i < 60:
    if (i % 2 == 1) :
        odd.append(i)
    
    i=i+1

# print the contents of the list
print('Odd minutes = {}'.format(odd))

right_now_minute = datetime.today().minute

if right_now_minute in odd:
    print('This is odd time')
else:
    print('Not an odd time')