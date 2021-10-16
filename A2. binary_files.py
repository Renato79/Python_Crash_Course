pathfile = 'test_files/binary.txt'

zen_of_python = [
    'Beautiful is better than ugly.',
    'Explicit is better than implicit.',
    'Simple is better than complex.',
    'Complex is better than complicated.',
    'Flat is better than nested.',
    'Sparse is better than dense.',
    'Readability counts.',
    'Special cases aren\'t special enough to break the rules.',
]



with open(pathfile, 'wb') as file_object:
    file_object.write(zen_of_python[0].encode(''))



# print(zen_of_python[0].encode())