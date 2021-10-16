# Writing to an Empty File
#
# To write text to a file, you need to call open() with a second argument
# telling Python that you want to write to the file. 
# 
# To see how this works, let’s write a simple message and store it in a
# file instead of printing it to the screen:
filename = 'test_files/writing.txt'

with open(filename, 'w') as file_object:
    file_object.write("Now is better than never.")

# The second argument, 'w', tells Python that we want to open the file
# in write mode.


# NOTE:
#
# You can open a file in:
#
# read mode ('r'), write mode ('w'), append mode ('a'), 
# 
# or a mode that allows you to read and write to the file ('r+'). 
# 
# If you omit the mode argument, Python opens the file in read-only mode by default.
#
# The open() function automatically creates the file you’re writing to
# if it doesn’t already exist. 
# 
# However, be careful opening a file in write mode ('w') because 
# if the file does exist, Python will erase the contents of the file 
# before returning the file object.

# NOTE 2:
#
# Python can only write strings to a text file. If you want to store 
# numerical data in a text file, you’ll have to convert the data to 
# string format first using the str() function.

# NOTE 3:
#
# The write() function doesn’t add any newlines to the text you write.
# So if you write more than one line without including newline 
# characters, your file may not look the way you want it
with open(filename, 'w') as file_object:
    file_object.write('Flat is better than nested.')
    file_object.write('Sparse is better than dense.')
    file_object.write('Errors should never pass silently.')

# Result:
# Flat is better than nested.Sparse is better than dense.Errors should never pass silently.

# Let's add newline carachters:
with open(filename, 'w') as file_object:
    file_object.write('Flat is better than nested.\n')
    file_object.write('Sparse is better than dense.\n')
    file_object.write('Errors should never pass silently.\n')
# Result:
# Flat is better than nested.
# Sparse is better than dense.
# Errors should never pass silently.




# Appending to a File
#
# If you want to add content to a file instead of writing over existing
# content, you can open the file in append mode.
#
with open(filename, 'a') as file_object:
    file_object.write('Beautiful is better than ugly.\n')
    file_object.write('Explicit is better than implicit.\n')
    file_object.write('Simple is better than complex.\n')





# check for testing purpose
with open(filename) as file_object:
    content = file_object.read()
print(content)