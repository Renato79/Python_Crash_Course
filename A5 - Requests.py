"""
Get source code from webpage

Needs to use pip3 install requests

If domain doesn't exists will show the message:

"Domain doesn't exist."

"""

import requests

#the required first parameter of the 'get' method is the 'url':



try:
    x = requests.get('http://www.renato.com')
    print(x.status_code) # result, simply the status code: 200
except:
    print("Domain doesn't exist.")