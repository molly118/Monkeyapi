# -*- coding: utf-8 -*-
import requests
import time
import unittest
from publicfunc import get_story_id, get_users_ids, get_stories_ids, get_stickers_story_id, get_ama_story_id
from gettoken import get_headers

# headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1MjY2MDMwLCJzdWIiOiI1MjY2MDMwIiwiaWF0IjoxNTYxNTM2NDI5LCJleHAiOjE1NjY3MjA0Mjl9.QR_sNty_yTXGStxBRoA8DJnT3LSyUm0_-161D0__OT0'}


class TestMoment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # headers = get_headers()
        print('this is setup func')

    @classmethod
    def tearDownClass(cls):
        print('this is teardown func')

    @unittest.skip('have removed categories')
    def test_moment_category_get(self):
        # url = '/api/v2/stories/categories'
        pass

    @unittest.skip('have removed categories')
    def test_moment_category_list_get(self):
        # url = '/api/v2/stories/categories/{categoryId}/stories?extras={extras}'
        pass

    def test_moment_watched_post(self):
        headers = get_headers()
        story_id = str(get_story_id())
        url = 'http://test.monkey.cool/api/v2/stories/' + story_id + '/watched'
        payload = {'watched_duration': 34.5,
                   'watch_source_type': ''}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    def test_moment_like_post(self):
        headers = get_headers()
        story_id = str(get_story_id())
        url = 'http://test.monkey.cool/api/v2/stories/' + story_id + '/like'
        r = requests.post(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    @unittest.skip('have removed categories')
    def test_moment_cate_info_get(self):
        # url = '/api/v2/stories/categories/{id}'
        pass

    def test_moment_one_info_get(self):
        headers = get_headers()
        story_id_int = get_story_id()
        story_id = str(story_id_int)
        url = 'http://test.monkey.cool/api/v2/stories/' + story_id
        r = requests.get(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(story_id_int, result['id'])
        # print(result['id'])

    @unittest.skip('have executed on test_msg module')
    def test_moment_send_dm_post(self):
        # url = '/api/v2/stories/{storyId}/dm'
        pass

    def test_moment_list_sb_get(self):
        headers = get_headers()
        users_ids = get_users_ids()[1].split(',')
        # print(users_ids[1])
        url = 'http://test.monkey.cool/api/v2/stories/users/' + users_ids[1] + '?page=0'
        r = requests.get(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_moment_likeuser_list_get(self):
        headers = get_headers()
        story_id_like = str(moment_post(self))
        # print('story_id_like', story_id_like)
        url = 'http://test.monkey.cool/api/v2/stories/' + story_id_like + '/like?page=0'
        r = requests.get(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        moment_del_delete(self, story_id_like)

    def test_moment_report_post(self):
        headers = get_headers()
        story_id_report = str(moment_post(self))
        # print('story_id_report', story_id_report)
        url = 'http://test.monkey.cool/api/v2/stories/' + story_id_report + '/report'
        payload = {'reason': 'Violence or Weaponry',
                   'source': 'moment'}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])
        moment_del_delete(self, story_id_report)

    def test_moment_info_me_get(self):
        headers = get_headers()
        story_id_me = str(moment_post(self))
        # print(story_id_me)
        url = 'http://test.monkey.cool/api/v2/stories/me?ids=' + story_id_me
        # print(url)
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        # print(data[0]['id'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(int(story_id_me), data[0]['id'])
        moment_del_delete(self, story_id_me)

    def test_moment_answer_post(self):
        headers = get_headers()
        story_sticker_id = str(get_stickers_story_id(5266030, 0)[0])
        # print(story_sticker_id)
        if len(story_sticker_id) != 0:
            url = 'http://test.monkey.cool/api/v2/stories/' + story_sticker_id + '/questions/answer'
            payload = {'question': 'Ask me a question',
                       'msg': 'This is test QS'}
            r = requests.post(url, headers=headers, json=payload)
            # result = r.json()
            # print(result)
            statuscode = r.status_code
            self.assertEqual(200, statuscode)
        else:
            print('didnt post stickers story')

    def test_moment_sb_recent_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/stories/users/5266030/recent'
        r = requests.get(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_moment_nearby_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/stories/nearby'
        payload = {'latitude': 39.92009210757688, 'longitude': 116.4281540336942}
        r = requests.get(url, params=payload, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_moment_infos_get(self):
        ids = ','.join(get_stories_ids())
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/stories?ids=' + ids
        r = requests.get(url, headers=headers)
        result = r.json()
        data = result['data']
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)

    def test_moment_send_ama_post(self):
        headers = get_headers()
        story_ama_id = str(get_ama_story_id(5266030, 0)[0])
        if len(story_ama_id) != 0:
            url = 'http://test.monkey.cool/api/v2/stories/' + story_ama_id + '/ama'
            payload = {'msg': 'snapchat or instagram?'}
            r = requests.post(url, headers=headers, json=payload)
            result = r.json()
            # print(result)
            statuscode = r.status_code
            self.assertEqual(200, statuscode)
            self.assertEqual(1, result['result'])
        else:
            print('didnt post ama story')

    def test_moment_ama_list_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/ama'
        r = requests.get(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        # print(result)
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(result['data'])


def moment_post(self):
    headers = get_headers()
    url = 'http://test.monkey.cool/api/v2/stories/'
    payload = {'category_id': 14,
               'video_size': 4325,
               'stickers': "[{'type': 1, 'layerIndex': 1, 'rotation': 0.0, 'sideScale': 1.5, 'xRatio': 0.5, 'yRatio': 0.5, 'questionTitle': 'Ask me a question', 'theme': 1}]",
               'video_text': 'this is a story',
               'latitude': 39.9200574,
               'longitude': 116.427477,
               'allow_nearby': 0,
               'cover_text': 'Thisistestcover'}
    r = requests.post(url, headers=headers, json=payload)
    result = r.json()
    print('postid', result['id'])
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    self.assertIsNotNone(result['id'])
    return result['id']


def moment_del_delete(self, storyid):
    headers = get_headers()
    # story_id = str(self.moment_post())
    print('del', storyid)
    url = 'http://test.monkey.cool/api/v2/stories/' + storyid
    r = requests.delete(url, headers=headers)
    result = r.json()
    # print(result)
    statuscode = r.status_code
    self.assertEqual(200, statuscode)
    self.assertEqual(1, result['result'])


if __name__ == '__main__':
    unittest.main()
