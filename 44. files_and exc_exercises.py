# 10-1. Learning Python: Open a blank file in your text editor and write
# a few lines summarizing what you’ve learned about Python so far. 
# Start each line with the phrase In Python you can. . .. Save the file
# as learning_python.txt in the same directory as your exercises from 
# this chapter. Write a program that reads the file and prints what you
# wrote three times. Print the contents once by reading in the entire 
# file, once by looping over the file object, and once by storing the
# lines in a list and then working with them outside the with block.

path = 'test_files/file_1.txt'

# reading in the entire file
with open(path) as file_object:
    content = file_object.read()
    print(f"{content}\n")

# looping over the file object
with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())

# storing the lines in a list and then working with them outside the 
# with block
with open(path) as file_object:
    my_arr = file_object.readlines()

for line in my_arr:
    print(line.strip())







# 10-2. Learning C: You can use the replace() method to replace any 
# word in a string with a different word. Here’s a quick example 
# showing how to replace 'dog' with 'cat' in a sentence:

# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

# Read in each line from the file you just created, learning_python.txt,
# and replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.
print("\n\nReplacing words:\n\n")

with open(path) as file_object:
    for line in file_object:
        if "never" in line:
            print(line.replace('never', 'AHAHAHAHAHAHAH').strip())
        else:
            print(line.strip())