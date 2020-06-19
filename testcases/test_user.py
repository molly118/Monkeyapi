# -*- coding:utf-8 -*-
import requests
import unittest
import json
from publicfunc import get_users_ids
from gettoken import get_headers


class TestUserInfo(unittest.TestCase):
    def test_me_info_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/me'
        payload = {'fields': 'user,userProfile,userCommon,userMatch,userStory,userBanana'}
        r = requests.get(url, headers=headers, params=payload)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['unique_name'], 'user name is not none')
        # print(result)

    def test_one_user_info_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5266030'
        payload = {'fields': 'user,userProfile,userCommon,userMatch,userStory,userRelation,ringStatus'}
        r = requests.get(url, headers=headers, params=payload)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_more_users_infos_get(self):
        headers = get_headers()
        more_users_ids = get_users_ids()[1]
        # print(more_users_ids)
        url = 'http://test.monkey.cool/api/v2/users?ids=' + more_users_ids + '&fields=user,userProfile,userCommon,userMatch,userStory,userRelation,ringStatus'
        # print(url)
        r = requests.get(url, headers=headers)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)


if __name__ == '__main__':
    unittest.main()
