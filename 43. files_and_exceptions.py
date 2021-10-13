# A relative file path tells Python to look for a given location 
# relative to the directory where the currently running program 
# file is stored.
# i.e.: with open('text_files/filename.txt') as file_object:

# You can also tell Python exactly where the file is on your computer
# regardless of where the program that’s being executed is stored. 
# This is called an absolute file path. 
# You use an absolute path if a relative path doesn’t work.
# i.e.: file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
#       with open(file_path) as file_object:

print("\nRead entire content:\n")
# READ ENTIRE CONTENT
path = 'test_files/'

with open(f"{path}file_1.txt") as file_object: 
    content = file_object.read() 
# read() reads the entire contents of the file
# and store it as one long string in contents

print(content)

# NOTE:

# file_object is an alias, I tried my_friend and it works.
# open('pi_digits.txt') returns an object representing pi_digits.txt. 
# Python assigns this object to file_object,

# NOTE:

# with
#
# The keyword with closes the file once access to it is no longer needed.
# Notice how we call open() in this program but not close(). You could
# open and close the file by calling open() and close(), but if a bug in
# your program prevents the close() method from being executed, the file
# may never close. This may seem trivial, but improperly closed files can
# cause data to be lost or corrupted. And if you call close() too early
# in your program, you’ll find yourself trying to work with a closed file
# (a file you can’t access), which leads to more errors. It’s not always 
# easy to know exactly when you should close a file, but with the 
# structure shown here, Python will figure that out for you. All you have
# to do is open the file and work with it as desired, trusting that Python
# will close it automatically when the with block finishes execution.

# The only difference between this output and the original file is the
# extra blank line at the end of the output. The blank line appears 
# because read() returns an empty string when it reaches the end of the
# file; this empty string shows up as a blank line. If you want to 
# remove the extra blank line, you can use rstrip() in the call to print():
# print(content.rstrip())






print("\nRead line by line:\n")

# READ LINE BY LINE
path = 'test_files/'

with open(f"{path}file_1.txt") as file_object:   
    for line in file_object:
        print(line.rstrip())
# NOTE: These blank lines appear because an invisible newline character is at
# the end of each line in the text file. The print function adds its own
# newline each time we call it, so we end up with two newline characters
# at the end of each line: one from the file and one from print(). Using
# rstrip() on each line in the print() call eliminates these extra blank 
# lines.



# NOTE: various tests
# my_list = []
# print(type(my_list)) - result: <class 'list'>
# print(type(content)) - result: <class 'str'>







print("\nMaking a List of Lines from a File:\n")

# Making a List of Lines from a File

with open(f"{path}file_1.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# print(type(lines)) - result: <class 'list'>

# readlines() method takes each line from the file and stores it in a list







print("\nMaking a List of Lines from a File:\n")

# Working with a File’s Contents

# We’ll attempt to build a single string containing all the digits in 
# the file with no whitespace in it (whitepace is new line in this example):
with open('test_files/file_1.txt') as file_object:
    lines = file_object.readlines()

string = ''

for line in lines:
    string += line.strip()
# The variable pi_string contains the whitespace that was on the left 
# side of the digits in each line, but we can get rid of that by using 
# strip() instead of rstrip():

print(string)
print(len(string))

# string = ''
# print(type(string))  - result: <class 'str'>


# NOTE:
#
# When Python reads from a text file, it interprets all text in the 
# file as a string. If you read in a number and want to work with that
# value in a numerical context, you’ll have to convert it to an integer
# using the int() function or convert it to a float using the float() function.








print("\nMaking a List of Lines from a File:\n")

# Large Files: One Million Digits
#
# So far we’ve focused on analyzing a text file that contains only three
# lines, but the code in these examples would work just as well on much
# larger files. If we start with a text file that contains pi to 
# 1,000,000 decimal places instead of just 30, we can create a single
# string containing all these digits. We don’t need to change our 
# program at all except to pass it a different file. We’ll also print
# just the first 50 decimal places, so we don’t have to watch a million
# digits scroll by in the terminal:
new_string = ''

for line in lines:
    new_string += line.strip()

print(f"{new_string[:52]}...")
print(len(new_string))


# NOTE:
#
# Python has no inherent limit to how much data you can work with; you 
# can work with as much data as your system’s memory can handle.








print("\nLooking for text in lines:\n")

# Looking for text in lines:
word = "never"
line_num = 0 # line number

for line in lines:
    line_num += 1
    if word in line:
        print(f"{line_num}: Found!")