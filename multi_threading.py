#!/usr/bin/env python3

import os
import threading
from datetime import datetime
from random import random, randint
import time
import math

def task_1(num_to_square:int) -> None:
    TASK_1_ID = 'Task 1'
    print('{}: ID of process running {} : {}'.format(time.ctime(), TASK_1_ID, os.getpid()))
    print('{}: {} assigned to thread: {}'.format(time.ctime(), TASK_1_ID, threading.current_thread().name))
    random_delay_secs:float = random() * 30
    time.sleep(random_delay_secs)
    print(f'\n{time.ctime()}: {TASK_1_ID} calculating Square in {random_delay_secs} seconds')
    sq = num_to_square * num_to_square
    print(f'{time.ctime()}: Square of {num_to_square}={sq}\n')

def task_2(num_to_cube:int) -> None:
    TASK_2_ID = 'Task 2'
    print('{}: ID of process running {}: {}'.format(time.ctime(), TASK_2_ID, os.getpid()))
    print('{}: {} assigned to thread: {}'.format(time.ctime(), TASK_2_ID, threading.current_thread().name))
    random_delay_secs:float = random() * 30
    time.sleep(random_delay_secs)
    print(f'\n{time.ctime()}: {TASK_2_ID} calculating Cube in {random_delay_secs} seconds')
    cube = math.pow(num_to_cube, 3)
    print(f'{time.ctime()}: Cube of {num_to_cube}={cube}\n')

def main():
    # print ID of current process
    print('{}: ID of process running main program: {}'.format(time.ctime(), os.getpid()))
  
    # print name of main thread
    print('{}: Main thread name: {}'.format(time.ctime(), threading.current_thread().name))

    t1 = threading.Thread(target=task_1, name='thread_1', args=(randint(0,100),))
    t2 = threading.Thread(target=task_2, name='thread_2', args=(randint(0,100),))

    # start threads
    t1.start()
    t2.start()
    print(f'{time.ctime()}: Main thread has started {t1.name} & {t2.name}')

    # wait till threads finish
    t1.join()
    t2.join()
    print(f'{time.ctime()}: Main thread has waited till finishing threads: {t1.name} & {t2.name}')

if __name__ == '__main__':
    main()