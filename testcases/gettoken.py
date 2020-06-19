# -*- coding: utf-8 -*-
import requests
# import json
from enbanana import encrypt

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1MjY2MTA2LCJzdWIiOiI1MjY2MTA2IiwiaWF0IjoxNTYxMDAwNDE3LCJleHAiOjE1NjYxODQ0MTd9.wM_AmlMA9Th69ZkWNZC5FhdcEFFzA9U62RWEujsCH7Q'}

'''
def get_token():
    url = 'http://test.monkey.cool/api/v1.0/auth/accountkit'

    headers = {
        'device': 'iOS',
        'User-Agent': 'Sandbox/5.3.5 (cool.monkey.ios; build:140; iOS 11.3.1) Alamofire/4.8.2',
        'timezone': '8',
        'version': '5.3.5',
        'Authorization': Authorization,
        'Host': 'test.monkey.cool',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5'
    }

    headers = {'Device': 'ios', 'Version': '5.4.4',
               'Client': 'test.monkey.cool',
               'Content-Type': 'application/json',
               'Accept': 'application/vnd.api+json, application/json',
               'source': '2pinvite1:794'}

    data = {'accountkit_token': 'EMAWdbLgL0H2CqZBYwschRTloL9It0RrZCmiqIQVZBPqCOVTo7fjjUCnIUt4PuZAZA5FpiprEPbEcjWZC2oMVdCZCy469spRjLuZBUevXLz5UMnQZDZD'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)
    r = requests.post(url, json=data, headers=headers)
    # conver to dict
    # print(r.json())
    dict = r.json()
    # print(dict['data']['attributes']['token'])
    token = dict['data']['attributes']['refresh_token']
    # user_id = dict['data']['relationships']['user']['data']['id']
    # conver to dict 2
    # text = r.text
    # print(json.loads(r.text))
    return token
    '''


def get_token():
    pass


token = ''

'''
def get_headers():
    if len(token) != 0:
    url = 'http://test.monkey.cool/api/v2/auth/login'
    payload = {'username': 'hahaprofile', 'password': 'Hahaprofile123'}
    r = requests.post(url, json=payload)
    result = r.json()
    # print(result)
    token = result['token'] 
    return headers = {'Device': 'ios', 'Version': '5.4.4',
                      'Client': 'test.monkey.cool',
                      'Content-Type': 'application/json',
                      'Accept': 'application/vnd.api+json, application/json',
                      'Authorization': 'Bearer ' + token,
                      'source': '2pinvite1:794'}
'''

headers = {'Device': 'ios', 'Version': '5.4.4',
           'Client': 'test.monkey.cool',
           'Content-Type': 'application/json',
           'Accept': 'application/vnd.api+json, application/json',
           'source': '2pinvite1:794'}


def get_headers():
    if 'Authorization' in headers:
        return headers
    url = 'http://test.monkey.cool/api/v2/auth/login'
    payload = {'username': 'yuanwang', 'password': 'yuanwang1'}
    r = requests.post(url, json=payload)
    result = r.json()
    # print(result)
    tokenstr = result['token']
    headers['Authorization'] = 'Bearer ' + tokenstr
    banana = encrypt()
    headers['banana'] = banana
    return headers

'''
def get_banana():
    banana = encrypt()
    headers['banana'] = banana
    return headers
'''
