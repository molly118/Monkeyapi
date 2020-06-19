# -*- coding: utf-8 -*-
import requests
import unittest
from publicfunc import get_headers


class TestUserPrivilege(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setup func')

    @classmethod
    def tearDownClass(cls):
        print('this is teardown func')

    def test_ups_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/ups'
        r = requests.get(url, headers=headers)
        result = r.json()
        print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_ups_privilege_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/ups/2'
        # payload = {'privilege': 2}
        r = requests.post(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)


if __name__ == '__main__':
    unittest.main()
