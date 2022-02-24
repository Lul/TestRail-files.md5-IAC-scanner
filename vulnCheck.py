import requests
import re

keywords = ['username', 'password', 'PRIVATE KEY']
server = input('Server in http:// or https:// format: ')
if server[-1] != '/':
    server+='/'

r = requests.get(f'{server}files.md5')
files = re.split(r'\n|  ', r.text)

for index, value in enumerate(files):
    if index % 2 != 0:
        r = requests.get(f'{server}{value}')
        if 'No direct script access allowed' not in r.text and 'Directory Listing Denied' not in r.text:
            if r.status_code != 500:
                for key in keywords:
                    if key in r.text:
                        print(f'{server}{value} - Status Code: {r.status_code} - INTERESTING KEYWORD: {key}')
                    else:
                        print(f'{server}{value} - Status Code: {r.status_code}')
                        break
