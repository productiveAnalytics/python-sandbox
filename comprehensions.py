generic_list = ['0.00', 1, 'Three', 5, '7', 9, 11.01, '13', 15]
print('Orig List = ', generic_list)
int_sqr_list = [e ** 2 for e in generic_list if (type(e) == int)]
print('Int Squares = ', int_sqr_list)

print()
print()

def transform(value) :
    """ Transforms boolean True as Y and False as N. For non-bool, returns original value """
    
    if type(value) == bool :
        return ('Y' if value == True else 'N')
    else :
        return value
    
capital_info = { 'State_ID': 'CO',
                 'State':'Colorado',
                 'Capital': 'Denver',
                 'Population': 1500000, 
                 'University_Town': True, 
                 'Business_Center': True, 
                 'Timezone': 'MT'}
from pprint import pprint
pprint(capital_info)
# Use comprehension to print True as Y and False as N, for others don't transform
cap_list = [transform(val) for (key, val) in capital_info.items()]
print('Capital info (list) = ', cap_list)

print()
print()

# Start with mix-type list
my_primes = [1, '2', '3', 5, '7', 11, 13, '17', 19]
print(my_primes)
try :
    csv_repr = ', '.join(my_primes)
except TypeError :
    print('As expected, could not Join mix-typed list. Converting to Str individually...')
    csv_repr = ', '.join(str(x) for x in my_primes)
    
print('CSV repr = ', csv_repr)