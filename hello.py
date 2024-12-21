#!.usr/bin/env python3

import requests

x = requests.get('https://google.com')

if x.status_code == 200:
    print('yay!')
else:
    print('uh-oh!')