import time
from functools import wraps

my_range = range(1000000)

def calc_exec_duration(funct_purpose : str) -> None:
    """ Wraps the given function in Start and End time to calculate the execution duration """
    
    def decorator_calc_exec_duration(funct):

        @wraps(funct)
        def calc_duration(rng: range):
			# this is the workhorse function that does actual work. Note the signature matches w/ actual function to be wrapped
            start_time = int(round(time.time() * 1000))
            funct(rng)
            finish_time = int(round(time.time() * 1000))
            print()
            print('{0} : {1} - {2} = {3}'.format(funct_purpose, start_time, finish_time, finish_time-start_time))
            print()

        return calc_duration

    return decorator_calc_exec_duration
    

@calc_exec_duration('listcomp')
def exec_listcomp(rng: range) -> None:
    try :
        # use listcomp
        for sqr in [x**2 for x in my_range if x % 2 == 1] :
            print(sqr, end=',')
    except Exception as ex :
        print('Exception occurred : '+ ex.message)

     
@calc_exec_duration('generator')
def exec_generator(rng: range) -> None:
    try :
        # use generator
        for sqr in (x**2 for x in my_range if x % 2 == 1) :
            print(sqr, end=',')
    except Exception as ex :
        print('Exception occurred : '+ ex.message)
    
    
print('------------------')
exec_listcomp(my_range)  
print()
print()
exec_generator(my_range)
print('------------------')