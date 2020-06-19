# coding=utf-8
import requests
import json


class BaseRequest:
    """

    """
    def send_post(self, url, data):
        """
        send post request
        """
        r = requests.post(url=url, data=data).text
        return r

    def send_get(self, url, data):
        """
        send get request
        """
        r = requests.get(url=url, params=data).text
        return r

    def run_main(self, method, url, data):
        """
        send post and get method
        """
        if method == 'get':
            r = self.send_get(url, data)
        else:
            r = self.send_post(url, data)
        try:
            r = json.loads(r)
        except:
            print('this is a text result')
        return r

base_request = BaseRequest()