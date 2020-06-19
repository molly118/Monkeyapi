# -*- coding: utf-8 -*-

import requests
import unittest
from gettoken import get_headers


class TestGeneral(unittest.TestCase):
    def test_update_config_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/general/appUpdateConfig'
        payload = {'deviceType': 'ios', 'version': '5.4.8'}
        r = requests.get(url, headers=headers, params=payload)
        result = r.json()
        # print(result['result'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        if result['result'] == 1:
            self.assertEqual(1, result['result'])
        elif result['result'] == 0:
            self.assertEqual(0, result['result'])
        else:
            print('failed')

    def test_general_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v3/stories/general'
        r = requests.get(url, headers=headers)
        result = r.json()
        # first, secondprint(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])


if __name__ == '__main__':
    unittest.main()
