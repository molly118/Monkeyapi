# -*- coding: utf-8 -*-

import requests
import unittest
from gettoken import get_headers

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1MjY2MDMwLCJzdWIiOiI1MjY2MDMwIiwiaWF0IjoxNTYxNTMwMDE5LCJleHAiOjE1NjY3MTQwMTl9.IkNJdZIJd09Q_4M8zC4_xO1NaNZKw_T0HAn_2P5naeQ'}


class TestConfig(unittest.TestCase):
    def test_config_filters_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/configuration/filters'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        data = result['data']
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)

    def test_config_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/configuration/'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        # print(result['convo_tips'])
        self.assertIsNotNone(result['convo_tips'])

    def test_config_story_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/configuration/story'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result['expire_at'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(85440, result['expire_at'])

    def test_config_servertime_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/configuration/servertime'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result['result'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    def test_config_famous_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/configuration/famous'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        # print(data)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)

    def test_config_v3_resource_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resources'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['data'])

    def test_config_v3_resource_questions_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=questions'
        r = requests.get(url, headers=headers)
        result = r.json()
        print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['data'])

    def test_config_v3_resource_ama_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=ama'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['ama']['resource_data'])

    def test_config_v3_resource_channels_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=channels'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        data = result['data']
        # print(data['channels']['resource_data'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['channels']['resource_data'])

    def test_config_v3_resource_famous_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=famous'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['famous']['resource_data'])

    def test_config_v3_resource_filters_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=filter'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['filters']['resource_data'])

    def test_config_v3_resource_chat_tips_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=chat_tips'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['chat_tips']['resource_data'])

    def test_config_v3_resource_match_event_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=match_event'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['match_event']['resource_data'])

    def test_config_v3_resource_famous_tips_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=famous_tips'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['famous_tips']['resource_data'])

    def test_config_v3_resource_ban_tips_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=ban_tips'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['ban_tips']['resource_data'])

    def test_config_v3_resource_launchnotice_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=launchnotice'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['launchnotice']['resource_data'])

    def test_config_v3_resource_match_tips_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/resource?resourceNames=match_tips'
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data['match_tips']['resource_data'])

    def test_config_v3_general_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/generalConfigs'
        r = requests.get(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['data'])

    def test_config_v3_twop_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/configuration/twoPConfigs'
        r = requests.get(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['data'])


if __name__ == '__main__':
    unittest.main()
