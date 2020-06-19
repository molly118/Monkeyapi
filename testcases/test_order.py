# -*- coding: utf-8 -*-

import requests
import unittest
from gettoken import get_headers


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.headers = get_headers()

    def tearDown(self):
        print('this is teardown')

    def test_orders_create_post(self):
        # headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/orders'
        payload = {'product_id': 1, 'pay_channel': 1}
        r = requests.post(url, headers=self.headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        if result['result'] == 1:
            self.assertEqual(200, statuscode)
        else:
            print(result)
        return result['data']

    @unittest.skip('cannot get token now')
    def test_orders_finish_post(self):
        '''
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/orders/finish'
        payload = {'order_id': , 'token': ''}
        r = requests.post(url, headers=headers, json=payload)
        '''


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.headers = get_headers()

    def tearDown(self):
        print('this is teardown')

    @unittest.skip('')
    def test_products_get(self):
        '''
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/products'
        r = requests.get(url, headers=headers)
        result = r.json()
        print(result)
        '''

    def test_products_type_1_get(self):
        # headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/products/1'
        r = requests.get(url, headers=self.headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_products_type_2_get(self):
        # headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/products/2'
        r = requests.get(url, headers=self.headers)
        result = r.json()
        data = result['data']
        # print(data[0]['function_type'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)
        self.assertEqual(2, data[0]['function_type'])


if __name__ == '__main__':
    unittest.main()
