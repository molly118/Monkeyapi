# -*- coding: utf-8 -*-
import requests
import time
import json
# from publicfunc import get_me_id, get_convo_id, get_users_ids
from gettoken import get_token, get_headers


# token = get_token()
# headers = {'Authorization': 'Bearer' + token}
# print(headers)
'''
def get_user_id():
    url = 'http://test.monkey.cool/api/v2/conversations/recent?updatedAtOpen=&updatedAtCollapsing=&loadOpen=true&loadCollapsing=true&type=1'
    r = requests.get(url, headers=headers)
    result = r.json()
    chat_user_id = result['data'][-1]['chat_user_id']
    return chat_user_id
    # print(result)
haha = get_user_id()


def get_users_ids():
        ids = []
        url = 'http://test.monkey.cool/api/v2/conversations/recent?updatedAtOpen=0&updatedAtCollapsing=0&loadOpen=true&loadCollapsing=true&type=1'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        for i in range(len(data)):
            id = data[i]['chat_user_id']
            sid = str(id)
            ids.append(sid)
        print(ids)
        # list to str
        more_ids = ','.join(ids)
        print(type(more_ids))
        return more_ids

print(get_users_ids())



def get_me_id():
    url = 'http://test.monkey.cool/api/v2/me?fields=user,userProfile,userCommon,userMatch,userStory,userBanana'
    r = requests.get(url, headers=headers)
    result = r.json()
    print(result)
    me_id = result['id']
    return me_id

meid = get_me_id()
print(type(meid))

timeStamp = 1561020122
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print (otherStyleTime)   # 2013--10--10 23:40:00

read_timestamp_sec = 1561020121528
read_timestamp = read_timestamp_sec / 1000
read_timestamp = 1561020122
time_array = time.localtime(read_timestamp)
read_time = time.strftime('%Y-%m-%d %H:%M:%S', time_array)
print(read_time)



def get_convo_id():
    """get a convation id."""
    url = 'http://test.monkey.cool/api/v2/conversations?modifiedAt='
    r = requests.get(url, headers=headers)
    result = r.json()
    print(result)
    convoid = str(result['data'][1]['conversation_id'])
    # print(convoid)
    return convoid

get_convo_id()


def get_senchat_user():
    unfollow_users = []
    url = 'http://test.monkey.cool/api/v2/users/search/username?page=&isHightlight='
    payload = {'name': 'h'}
    r = requests.post(url, headers=headers, json=payload)
    result = r.json()
    # print(result)
    data = result['data']
    for i in range(len(data)):
        id = data[i]['id']
        followstatus = data[i]['follow_status']
        if followstatus == 3:
            break
        unfollow_users.append(id)
    return unfollow_users

print(get_senchat_user())

def get_convo_id():
    """get a convation id."""
    url = 'http://test.monkey.cool/api/v2/conversations?modifiedAt='
    r = requests.get(url, headers=headers)
    result = r.json()
    print(result)
    convoid = str(result['data'][1]['conversation_id'])
    # print(convoid)
    return convoid

print(get_convo_id())



def test_chat_videocall_post():
    me_id = get_me_id()
    convo_id = get_convo_id()
    friend_id = convo_id.split(':')
    # print(friend_id[1])
    if convo_id[0] == me_id:
        url = 'http://test.monkey.coolapi/v2/videocall/miss/' + friend_id[1] + '/' + convo_id
        print(url)
        r = requests.post(url, headers=headers)
        result = r.json()
        print(result)
    else:
        url = 'http://test.monkey.coolapi/v2/videocall/miss/' + friend_id[0] + '/' + convo_id
        print(url)
        r = requests.post(url, headers=headers)
        print(r.url)
        result = r.json()
        print(result)

test_chat_videocall_post()

users_ids = get_users_ids()[1].split(',')
# print(type(users_ids[1]))

def get_story_id():
    """get a story id."""
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/users/5266030?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    # print(result)
    data = result['data']
    # print(data)
    story_id = data[0]['id']
    return story_id

print(get_story_id())



def get_story_id():
    """get a story id."""
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/users/5266030?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    # print(result)
    data = result['data']
    story_id = data[0]['id']
    return story_id

print(get_story_id())



def get_stories_ids():
    stories_ids = []
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/users/5266030?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        ids = data[i]['id']
        stories_ids.append(ids)
    print(stories_ids)

# print(get_stories_ids())
get_stories_ids()


def get_users_story_id(userid, nextpage):
    headers = get_headers()
    stickers_ids = []
    ama_ids = []
    # new_stickers = {}
    url = 'http://test.monkey.cool/api/v2/stories/users/' + str(userid) + '?page=%s' % str(nextpage)
    # print(url)
    r = requests.get(url, headers=headers)
    result = r.json()
    # print(result)
    data = result['data']
    for i in range(len(data)):
        story_stickers_id = data[i]['story_id']
        # print(data[i]['stickers'])
        if 'stickers' in data[i]:
            stickers = data[i]['stickers']
            new_stickers = json.loads(stickers)
            # 注释
            print('----------------------------')

            print(new_stickers)
            print(type(new_stickers))
            print('----------------------------')
            # new_stickers = stickers[2:-2]
            # 注释
            if new_stickers[0]['type'] == 1:
                stickers_ids.append(story_stickers_id)
            elif new_stickers[0]['type'] == 3:
                ama_ids.append(story_stickers_id)
    return stickers_ids, ama_ids


# get_users_story_id(users_ids[1])Zxcbn ./
hahha = get_users_story_id(5266030, 0)
print(hahha)

def get_followed_users(meid):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/users/' + str(meid) + '/followers?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    print(result)
    data = result['data']
    return data[0]

print(get_followed_users(5266126))



def search_result():
    headers = get_headers()
    user_ids = []
    url = 'http://test.monkey.cool/api/v2/users/search/username'
    data = {'name': 'haha'}
    r = requests.post(url, json=data, headers=headers)
    result = r.json()
    print(result)
    data = result['data']
    for i in range(len(data)):
        follow_status = data[i]['follow_status']
        if follow_status == 0 or follow_status == 2:
            userid = data[i]['id']
            user_ids.append(userid)
    return user_ids

print(search_result())
'''
li = ['4273', '127.0.0.1:6200', '4473']
print(len(li))
print(range(len(li)))
for i in li:
    print(i)