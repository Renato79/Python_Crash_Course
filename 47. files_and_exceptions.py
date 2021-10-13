# Exceptions
#
# Python uses special objects called exceptions to manage errors that
# arise during a program’s execution. Whenever an error occurs that 
# makes Python unsure what to do next, it creates an exception object.
# If you write code that handles the exception, the program will 
# continue running. If you don’t handle the exception, the program will
# halt and show a traceback, which includes a report of the exception 
# that was raised.
#
# Exceptions are handled with try-except blocks. A try-except block asks
# Python to do something, but it also tells Python what to do if an
# exception is raised. When you use try-except blocks, your programs 
# will continue running even if things start to go wrong. Instead of
# tracebacks, which can be confusing for users to read, users will see
# friendly error messages that you write.



# Handling the ZeroDivisionError Exception

#   Traceback (most recent call last):
#     File "/Users/rbianco/Desktop/reboot/Python Crash Course/47. files_and_exceptions.py", line 26, in <module>
#       print(5/0)
# ➊ ZeroDivisionError: division by zero
#
# print(5/0)

# The error reported at ➊ in the traceback, ZeroDivisionError, is an 
# exception object. Python creates this kind of object in response to
# a situation where it can’t do what we ask it to. When this happens,
# Python stops the program and tells us the kind of exception that was
# raised. We can use this information to modify our program. We’ll tell
# Python what to do when this kind of exception occurs; that way, if it
# happens again, we’re prepared.


# Using try-except Blocks
#
# When you think an error may occur, you can write a try-except block 
# to handle the exception that might be raised. You tell Python to try
# running some code, and you tell it what to do if the code results 
# in a particular kind of exception.
#
# Here’s what a try-except block for handling the ZeroDivisionError 
# exception looks like:
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")






# Using Exceptions to Prevent Crashes
#
# Handling errors correctly is especially important when the program has
# more work to do after the error occurs. This happens often in programs
# that prompt users for input. If the program responds to invalid input
# appropriately, it can prompt for more valid input instead of crashing.
#
# Let’s create a simple calculator that does only division:
# ... (code below)... then further notes:
#
# The else Block
#  This example also includes an else block. Any code that depends on 
# the try block executing successfully goes in the else block:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print(f"You cannot divide {first_number} by {second_number}!")
    else:
        print(answer)
