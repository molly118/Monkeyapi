# -*- coding: utf-8 -*-
import requests
import json
from gettoken import get_headers

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1MjY2MDMwLCJzdWIiOiI1MjY2MDMwIiwiaWF0IjoxNTYxNTM2NDI5LCJleHAiOjE1NjY3MjA0Mjl9.QR_sNty_yTXGStxBRoA8DJnT3LSyUm0_-161D0__OT0'}

'''
def get_headers():
    """get headers."""
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1MjY2MDMwLCJzdWIiOiI1MjY2MDMwIiwiaWF0IjoxNTYxNjMwOTYzLCJleHAiOjE1NjY4MTQ5NjN9.cx65RUsw87z8YrbFrLRKuAxJ5ALCWcdQEiS8p-yo-ZE'}
    return headers
'''

print(get_headers.__doc__)


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


print(get_story_id.__doc__)


def get_stories_ids():
    """get stories ids."""
    stories_ids = []
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/users/5266030?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        ids = str(data[i]['id'])
        stories_ids.append(ids)
    return stories_ids


print(get_stories_ids.__doc__)


def get_convo_id():
    """get a convation id."""
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/conversations?modifiedAt='
    r = requests.get(url, headers=headers)
    result = r.json()
    convoid = str(result['data'][1]['conversation_id'])
    # print(convoid)
    return convoid


print(get_convo_id.__doc__)


def get_me_id():
    """get me id."""
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/me?fields=user,userProfile,userCommon,userMatch,userStory,userBanana'
    r = requests.get(url, headers=headers)
    result = r.json()
    # print(result)
    me_id = result['id']
    return me_id


print(get_me_id.__doc__)


def get_stickers_story_id(userid, nextpage):
    """get stories with stickers."""
    headers = get_headers()
    stickers_ids = []
    url = 'http://test.monkey.cool/api/v2/stories/users/' + str(userid) + '?page=%s' % str(nextpage)
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        story_stickers_id = data[i]['story_id']
        # print(data[i]['stickers'])
        if 'stickers' in data[i]:
            # if data[i]['stickers'] in data[i]:
            stickers = json.loads(data[i]['stickers'])
            if stickers[0]['type'] == 1:
                stickers_ids.append(story_stickers_id)
    return stickers_ids


print(get_stickers_story_id.__doc__)


def get_ama_story_id(userid, nextpage):
    """get stories with ama."""
    headers = get_headers()
    ama_ids = []
    url = 'http://test.monkey.cool/api/v2/stories/users/' + str(userid) + '?page=%s' % str(nextpage)
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        story_stickers_id = data[i]['story_id']
        if 'stickers' in data[i]:
            stickers = json.loads(data[i]['stickers'])
            if stickers[0]['type'] == 3:
                ama_ids.append(story_stickers_id)
    return ama_ids


print(get_ama_story_id.__doc__)


def get_users_ids():
    """get different convo status users ids."""
    ids_zero = []
    ids_one = []
    ids_two = []
    ids_four = []
    ids_five = []
    ids_six = []
    ids_seven = []
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/conversations/recent?updatedAtOpen=0&updatedAtCollapsing=0&loadOpen=true&loadCollapsing=true&type=3'
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        id = data[i]['chat_user_id']
        status = data[i]['status']
        if status == 8 or status == 3:
            break
        elif status == 0:
            zid = str(id)
            ids_zero.append(zid)
        elif status == 1:
            oid = str(id)
            ids_one.append(oid)
        elif status == 2:
            tid = str(id)
            ids_two.append(tid)
        elif status == 4:
            fid = str(id)
            ids_four.append(fid)
        elif status == 5:
            fiid = str(id)
            ids_five.append(fiid)
        elif status == 6:
            sid = str(id)
            ids_six.append(sid)
        elif status == 7:
            seid = str(id)
            ids_seven.append(seid)
        # print(ids)
# NoRelation-0, Open-1, Collapsing-2, Deleted-3, PairInit-4, Pair-5, UnPair-6, ToNormal-7, Hide-8
    more_ids_zero = ','.join(ids_zero)
    more_ids_one = ','.join(ids_one)
    more_ids_two = ','.join(ids_two)
    more_ids_four = ','.join(ids_four)
    more_ids_five = ','.join(ids_five)
    more_ids_six = ','.join(ids_six)
    more_ids_seven = ','.join(ids_seven)

    return more_ids_zero, more_ids_one, more_ids_two, more_ids_four, more_ids_five, more_ids_six, more_ids_seven


print(get_users_ids.__doc__)


def get_domain():
    pass


def get_senchat_user():
    headers = get_headers()
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


def get_users_story_id(userid):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/users/' + userid + '?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()


def get_followed_users(meid):
    """get my follower."""
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/users/' + meid + '/followers?page=0'
    r = requests.get(url, headers=headers)
    result = r.json()
    data = result['data']
    return data[1]


print(get_followed_users.__doc__)


def search_unfollowing_result():
    user_ids = []
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/users/search/username'
    data = {'name': 'haha'}
    r = requests.post(url, json=data, headers=headers)
    # print(r.json())
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        follow_status = data[i]['follow_status']
        if follow_status == 0 or follow_status == 2:
            userid = data[i]['id']
            user_ids.append(userid)
    return user_ids[5]


def search_following_result():
    user_ids = []
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/users/search/username'
    data = {'name': 'haha'}
    r = requests.post(url, json=data, headers=headers)
    result = r.json()
    data = result['data']
    for i in range(len(data)):
        follow_status = data[i]['follow_status']
        if follow_status == 1:
            userid = data[i]['id']
            user_ids.append(userid)
    return user_ids[1]
