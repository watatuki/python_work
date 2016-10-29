#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import json
 
app_id = ""
app_secret = ""

data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}
params = {'location': 'New York',
          'term': 'pasta',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }
 
resp = requests.get(url=url, params=params, headers=headers)

jsdb = resp.json()

#print jsdb.dumps(jsonData, sort_keys = True, indent = 4)

#print jsdb.keys()

entries = jsdb['businesses']

#print entries

#for e in entries:
#    print "name :" + e['name']
#    l = e['coordinates']
#    print l['latitude']
#    print l['longitude']
#    print '\n'

import pprint
pprint.pprint(resp.json()['businesses'])
