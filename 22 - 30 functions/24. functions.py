# Returning a Simple Value 

def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')

print(musician)



# Making an Argument Optional
# default value needs to be moved to the end of the list of parameters
def full_name(fname, lname, mname=''): 
    # Python interprets non-empty strings as True
    if mname:
        full_name = f'{fname} {mname} {lname}'
    else:
        full_name = f"{fname} {lname}"
    
    return full_name.title()

# If we’re using a middle name, we have to make sure the middle name is
#the last argument passed so Python will match up the positional 
# arguments correctly.
musician = full_name('tommy', 'jones', 'lee')
print(musician)

musician = full_name('michael', 'jackson')
print(musician)




# Returning a Dictionary
def person_dict(first_name, last_name):
    person = {'fname': first_name, 'lname': last_name}
    return person

musician = person_dict('renato', 'bianco')
print(musician)



# Adding data to the function
def person_dictionary(first_name, last_name, age=None):
    person = {'fname': first_name, 'lname': last_name}
    
    if age:
        person['age'] = age
    
    return person

musician = person_dictionary('roger', 'waters', 78)

print(musician)