import os

# subfolder where file may reside
myFolder = 'Data'

def open_new_or_existing_file(filename : str) -> 'fhandle' :
	""" Try to open the file in x mode, 
		means if the file exists there would be error
		but if the file doesn't exists, the system opens in write mode.
		Otherwise open existing file in append mode """

        # change to Data subfolder
	os.chdir(myFolder)
	
	print('Present working directory : ', os.getcwd())
	abspath = os.path.abspath(filename);
	
	try:
		fhandle = open(filename, 'x')
		print('File does not exist, opening new : ', abspath)
	except FileExistsError:
		fhandle = open(filename, 'a')
		print('File {0} exist, appending to it...'.format(abspath))

	return fhandle


pwd = os.getcwd()
print('Present working directory : ', pwd)
    
with open_new_or_existing_file('todo.txt') as todo_file : 
    print('Read Head First Python book', file = todo_file)
    print('Review NumPy stack', file = todo_file)
    print('Study PMP course book', file = todo_file)
    print("Revisit Andrew Ng' ML course", file = todo_file)
    
with open('todo.txt', 'r') as myfile:
    i = 0
    for todo in myfile:
        i += 1
        print(i, ': ', todo, end = '\n\n') # add two lines
