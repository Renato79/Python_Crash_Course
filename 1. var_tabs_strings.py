first_name = "renato"
last_name = "bianco"

# Formats
full_name = f"{first_name} {last_name}"

print(full_name.title())

print(f"Hello {full_name.title()}!")

print(f"Here there is a tab \t{first_name} {last_name}")


# Tabs and newlines
print ("Here there is a \nnew\nline")

print("Languages:\n\tPython\n\tC\n\tJavaScript\n\tPerl")


# Stripping Whitespace
string = "  Python  "
# Right whitespaces:
print(f"{string.rstrip()}") # rstrip() doesn't change the variable
# Left whitespaces:
print(f"{string.lstrip()}") # lstrip() doesn't change the variable
# Stripping from both sides:
print(string.strip()) # strip() doesn't change the variable

# Stripping permanently
string = string.strip()

print(string)

message = 'Albert Einstein once said: “A person who never made a mistake never tried anything new.”'
print(message)




# You can assign values to more than one variable using just a single line.
x, y, z = 0, 0, 0

