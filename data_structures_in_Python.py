""" This program demonstrates built-in data structures : List, Tuple, Dictionary, Set """

# Empty List
myList = []
print ('Empty list = {} '.format(myList))

myList.append('DE')
myList.append('NV')
myList.append('WY')

print ('List of Pro business States = {0} '.format(myList))

print()

# Empty Tuple
myTuple = ()
print ('Empty tuple = {} '.format(myTuple))

print ('Tuple does not allow to add/delete/update item')
print ('Defining a new tuple...')
myTuple = ('i', 'u', 'e', 'o', 'a') # Jumbling to demo power of min/max
print ('Tuple of vowels = {0} '.format(myTuple))
print ('In Tuple, min=' + min(myTuple) + ', ' + 'max=' + max(myTuple))

sudo_vowel = ('y', ) # Note the syntax for one element Tuple 
print ('Tuple containing single sudo vowel = {0} '.format(sudo_vowel ))

print()

# Empty dictionary
dict = {} 
print ('Empty dictionary = {} '.format(dict))

dict['NY'] = 'Albany'
dict['NC'] = 'Raleigh'
dict['CO'] = 'Denver'
dict['IA'] = 'Des Moines'
dict['UT'] = 'SLC'
print ('Dictionary w/ capitals = {0} '.format(dict))

print()

# Empty Set
mySet = set()
print ('Empty set = {} '.format(mySet))

mySet.add('Yellowstone')
mySet.add('Grand Teton')
mySet.add('Yosemite')
mySet.add('Arches')
mySet.add('Zions')
mySet.add('Grand Canyon')
mySet.add('Olympic')
mySet.add('Acadia')
print ('Set w/ Parks = {0} '.format(mySet))