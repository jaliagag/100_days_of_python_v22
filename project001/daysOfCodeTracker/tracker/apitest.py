#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import json
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '...')
owner = 'jaliagag'
repo = '100_days_of_python_v22'
query_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
headers = {'Authorization': f'token {token}'}
params = {
    "author": "jaliagag",
}
r = requests.get(query_url, headers=headers, params=params).json()
#pprint(r)
#pprint(r[1])

for i in r:
#    print(i['html_url'])
#    print(i['commit'])
    print(i['commit']['author']['date'])
#    print(type(r[i]))
    #pprint(r[i['html_url']])
#    pprint(
#        r[-1]
#    )
