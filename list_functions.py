nums = [ 1, 2, 3, 4, 5]
print('Original list = {0}'.format(nums))

input_value = 0
index = 0
item_value = 0

# Append functionality
print('\n--------- Append ---------')
input_value = input("Enter number to Append to the list : ")
num_to_append = int(input_value)
nums.append(num_to_append)
print(nums)

# Remove functionality
print('\n--------- Remove ---------')
input_value = input("Enter number to Remove from the list : ")
num_to_remove = int(input_value)
if (num_to_remove not in nums) :
    print('{0} does not exist in list {1}'.format(num_to_remove, nums))
else :
    item_value = nums.remove(num_to_remove)
    print(nums)
    
# Insert functionality
print('\n--------- Insert ---------')
input_value = input("Enter [index,number] to Insert into the list : ")
input_list = input_value.split(",")
if len(input_list) >= 2 :
    index = int(input_list[0]) # first integer is index
    num_to_insert = int(input_list[1]) # second integer is actual value
#    if (0 <= index and index < len(nums)) :
    nums.insert(index, num_to_insert)
    print(nums)
#    else :
#        print('Index = {0} is out-of-bounds for list {1}'.format(index, nums))
        
# Pop functionality    
print('\n--------- Pop ---------')    
input_value = input("Enter index to Pop from the list (blank for default) : ")
if (len(input_value.strip()) == 0) :
    item_value = nums.pop() # use no-arg pop() function
    print('Popped last item {0} from the list'.format(item_value))
else :
    index = int(input_value.strip())
    if (0 <= index and index < len(nums)) :
        item_value = nums.pop(index) # use one-arg pop(index) function
        print('Popped item {0} from original index {1} from the list'.format(item_value, index))
    else : 
        print('Index = {0} is out-of-bounds for list {1}'.format(index, nums))
print(nums)

# list can be heterogeneous
print('\n--------- Heterogeneous List ---------') 
middle_index = (len(nums) // 2)
nums.insert(middle_index, 'half-way-thru')
print(nums)
