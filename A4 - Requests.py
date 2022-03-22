"""
Get source code from webpage

Needs to use pip3 install requests
"""

import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.status_code) # result, simply the status code: 200
print(x) # result: <Response [200]>
print(x.content) # result on one line: b'<!DOCTYPE html>\n<html>\n<body>\n\n<h1>This is a Test Page</h1>\n\n</body>\n</html>'
