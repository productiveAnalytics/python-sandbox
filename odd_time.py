from datetime import datetime

odd = [ 1, 3, 5, 7, 9,
       11, 13, 15, 17, 19,
       21, 23, 25, 27, 29,
       31, 33, 35, 37, 39,
       41, 43, 45, 47, 49,
       51, 53, 55, 57, 59 ]

right_now_minute = datetime.today().minute

if right_now_minute in odd:
    print('This is odd time')
else:
    print('Not an odd time')
