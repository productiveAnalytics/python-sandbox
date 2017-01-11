""" This code demonstrates 
	pass-by-value 
	or 
	pass-by-reference 
	for Python functions """

def duplicate (arg) :
    """ Doubles the provided arg (Number, String or List) and returns it """
    print('Before:', arg)
    arg = arg * 2
    print('After:', arg)
    return arg
    
def appendList (argList : list , suffix_words : str = "...Big Data!") -> list :
    """ Appends the given list by [optional] provided suffix_words. """
    print('Before:', argList)
    argList.append(suffix_words)
    print('After:', argList)
    return argList
    
print()

print("Checking doubleTheNumber(num) function for Number >>>")
in_1 = 13
out_1 = duplicate(in_1)
print('{0} * 2 = {1}'.format(in_1, out_1))

print("Checking doubleTheNumber(num) function for String >>>")
in_1 = 'CloneMe'
out_1 = duplicate(in_1)
print('{0} * 2 = {1}'.format(in_1, out_1))

print("Checking doubleTheNumber(num) function for String >>>")
in_1 = [1, 2, 3, 5, 7]
out_1 = duplicate(in_1)
print('{0} * 2 = {1}'.format(in_1, out_1))

print()

print("Checking appendList(aList, [suffix_word] function ---")
input_list = [1, 2, 3, 5, 7]
print('>>> 1. Input list = ', str(input_list))
input_suffix_words = input('Enter [optional] words to append. (Blank to use default words) : ')
output_list = []
suffix_provided = bool(input_suffix_words) # utilizing bool() which will return False if blank
if suffix_provided :
    output_list = appendList(input_list, input_suffix_words)
else :
    output_list = appendList(input_list)
print(str(input_list) + ' + '+ ('default' if suffix_provided else input_suffix_words ) + ' = ' + str(output_list))
print('Note that the input list has been changed during the function call - acting as by-reference!')
print('>>> 2. Input list = ', str(input_list))