# -*- coding:utf-8 -*-

import requests
# import gettoken
import unittest
import json
from gettoken import get_headers
from publicfunc import get_me_id, get_followed_users, search_following_result, search_unfollowing_result


class TestFollow(unittest.TestCase):
    def test_follow_origin_post(self):
        headers = get_headers()
        userid = str(search_unfollowing_result())
        url = 'http://test.monkey.cool/api/v2/users/' + userid + '/follow'
        payload = {'origin': '1'}
        r = requests.post(url, headers=headers, params=payload)
        # print(r.json())
        result = r.json()
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, result['result'])
    # follow and unfollow must be ordered to test

    def test_unfollow_post(self):
        userid = str(search_following_result())
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/' + userid + '/unfollow'
        r = requests.post(url, headers=headers)
        result = r.json()
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, result['result'])

    def test_follow_none_origin_post(self):
        # userid = str(self.search_result())
        headers = get_headers()
        meid = str(get_me_id())
        userid = str(get_followed_users(meid))
        url = 'http://test.monkey.cool/api/v2/users/' + userid + '/follow'
        r = requests.post(url, headers=headers)
        result = r.json()
        self.assertEqual(200, r.status_code)
        self.assertEqual(1, result['result'])

    @unittest.skip("    ")
    def test_ignore_follow_get(self):
        # userid = str(self.search_result)
        # url = 'http://test.monkey.cool/api/v2/me/followrequests/' + userid\
        #        + '/ignore'
        pass

    def test_following_list_get(self):
        headers = get_headers()
        me_id = str(get_me_id())
        url = 'http://test.monkey.cool/api/v2/users/' + me_id + '/followings?page=0'
        r = requests.get(url, headers=headers)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_follower_list_get(self):
        headers = get_headers()
        me_id = str(get_me_id())
        url = 'http://test.monkey.cool/api/v2/users/' + me_id + '/followers?page=0'
        r = requests.get(url, headers=headers)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_search_user_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/search/username'
        data = {'name': 'hahahuluhulu'}
        r = requests.post(url, json=data, headers=headers)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_follow_request_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/me/followrequests?page='
        r = requests.get(url, headers=headers)
        # print(r.json())
        result = r.json()
        self.assertIsNotNone(result['data'], 'search result is not none')
        # self.assertIsNone(result['data'])


class TestBlockReport(unittest.TestCase):
    def test_block_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5271463/block'
        r = requests.post(url, headers=headers)
        result = r.json()
        print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['block_status'])
    # block and unblock must be ordered to test

    def test_unblock_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5271463/unblock'
        r = requests.post(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        # self.assertEqual(0, result['block_status'])

    def test_blocklist_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/block-list'
        r = requests.get(url, headers=headers)
        # result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_report_otherprofile_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5271463/report'
        data = {'source': 'profile'}
        r = requests.post(url, headers=headers, json=data)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])


class TestHmu(unittest.TestCase):
    def test_click_hmu_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/me/hmu/click'
        r = requests.post(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        lastclick = result['last_click']
        # print(type(lastclick))
        if lastclick != 0:
            print('have printed it')
            # test_stop_hmu_delete(self)

    def test_hmu_list_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/follows/following/hmu'
        r = requests.get(url, headers=headers)
        result = r.json()
        # get the hmu list
        hmuusers = result['hmu_users']
        # print(hmuusers)
        # print(hmu_user_id)
        if len(hmuusers) == 0:
            test_mute_hmu_post(self)
            test_unmute_hmu_delete(self)
        else:
            # get fist user id in hmu list
            hmu_user_id = hmuusers[0]['user_id']
            test_dm_hmu_post(self, hmu_user_id)
            test_user_hmu_delete(self, hmu_user_id)
            test_mute_hmu_post(self)
            test_unmute_hmu_delete(self)

    def get_user_id(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/conversations/recent?updatedAtOpen=0&updatedAtCollapsing=0&loadOpen=true&loadCollapsing=true&type=1'
        r = requests.get(url, headers=headers)
        result = r.json()
        chat_user_id = result['data'][-2]['chat_user_id']
        return chat_user_id
        # print(result)

    def test_follow_v3_hmu_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/follows/following/hmu/{userId}/dm'        
        pass


def test_dm_hmu_post(self, hmu_user_id):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/follows/following/hmu/' + str(hmu_user_id) +'/dm'
    payload = {'msg': 'this is test dm'}
    r = requests.post(url, headers=headers, json=payload)
    # result = r.json()
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    print('test_dm_hmu_post')


def test_user_hmu_delete(self, hmu_user_id):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/follows/following/hmu/' + str(hmu_user_id)
    r = requests.delete(url, headers=headers)
    result = r.json()
    # print(result)
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    self.assertEqual(1, result['result'])


def test_mute_hmu_post(self):
    headers = get_headers()
    chat_user_id = str(self.get_user_id())
    url = 'http://test.monkey.cool/api/v2/follows/following/hmu/blocks/' + chat_user_id
    r = requests.post(url, headers=headers)
    statuscode = r.status_code
    result = r.json()
    print(result['data']['mute_status'])
    self.assertEqual(1, result['data']['mute_status'])
    self.assertEqual(200, statuscode)
    print('test_mute_hmu_post')


def test_unmute_hmu_delete(self):
    headers = get_headers()
    chat_user_id = str(self.get_user_id())
    url = 'http://test.monkey.cool/api/v2/follows/following/hmu/blocks/' + chat_user_id
    r = requests.delete(url, headers=headers)
    result = r.json()
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    self.assertEqual(0, result['block_status'])
    # print(result['block_status'])
    print('test_unmute_hmu_delete')


def test_stop_hmu_delete(self):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/me/hmu/click'
    r = requests.delete(url, headers=headers)
    result = r.json()
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    self.assertEqual('true', result['disabled'])
    print('test_stop_hmu_delete')


if __name__ == '__main__':
    unittest.main()
