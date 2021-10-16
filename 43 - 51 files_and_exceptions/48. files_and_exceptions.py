from typing import Container


filename = 'test_files/none.txt'
"""
with open(filename, encoding='utf-8') as f:
    contents = f.read()
"""
# NOTE: 
# There are two changes here. One is the use of the variable f to 
# represent the file object, which is a common convention. The second 
# is the use of the encoding argument. This argument is needed when 
# your system’s default encoding doesn’t match the encoding of the file
# that’s being read.

# The last line of the traceback reports a FileNotFoundError: this is 
# the exception Python creates when it can’t find the file it’s trying
# to open. In this example, the open() function produces the error, so
# to handle it, the try block will begin with the line that contains open():
my_file = "test_files/none.txt"

try:
    with open(my_file, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {my_file} does not exist.\n\n")







# The split() method separates a string into parts wherever it finds a 
# space and stores all the parts of the string in a list. The result is
# a list of words from the string, although some punctuation may also 
# appear with some of the words. To count the number of words in 
# Alice in Wonderland, we’ll use split() on the entire text. Then we’ll
# count the items in the list to get a rough idea of the number of words 
# in the text:
def count_word(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        pass # Failing Silently
        # print(f"Sorry, the book {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The book {filename.rsplit('/')[1]} has about {num_words} words.")

my_files = ['file_1.txt', 'guest_book.txt', 'guests.txt', 'my nice book', 'poll.txt', 'wizard.txt', 'writing.txt']

for book in my_files:
    count_word(f"test_files/{book}")

# NOTE:
# You could redirect any error to external file. missing.appen(filename)
#
# The pass statement also acts as a placeholder. It’s a reminder that 
# you’re choosing to do nothing at a specific point in your program’s
# execution and that you might want to do something there later. For
# example, in this program we might decide to write any missing 
# filenames to a file called missing_files.txt. Our users wouldn’t see
# this file, but we’d be able to read the file and deal with any missing texts.
