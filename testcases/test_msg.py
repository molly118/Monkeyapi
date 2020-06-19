# -*- coding: utf-8 -*-
import json
import unittest
import requests
# import time
# import datetime
from publicfunc import get_story_id, get_me_id, get_convo_id, get_users_ids, get_senchat_user
from gettoken import get_headers


class TestMsg(unittest.TestCase):

    def test_user_dm_default_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5270949/dm'
        payload = {'msg': 'This is a test msg', 'source_type': 0}
        r = requests.post(url, headers=headers, json=payload)
        # r = requests.post(url, headers=headers, data=json.dumps(payload))
        result = r.json()
        # result = r.text()
        # print(result)
        # print(result['result'])
        statuscode = r.status_code
        print(statuscode)
        self.assertEqual(200, statuscode)
        self.assertEqual(result['result'], 1)

    def test_user_dm_recent_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/users/5270949/dm'
        payload = {'msg': 'This is a test msg', 'source_type': 1}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result['result'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    def test_story_dm_post(self):
        headers = get_headers()
        stid = str(get_story_id())
        url = 'http://test.monkey.cool/api/v2/stories/' + stid + '/dm'
        # print(url)
        payload = {'msg': 'This is a test moment dm message'}
        r = requests.post(url, headers=headers, json=payload)
        statuscode = r.status_code
        result = r.json()
        # print(result)
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    @unittest.skip("to be tested later")
    def test_convo_friends_get(self):
        # url = 'http://test.monkey.cool/api/v2/conversations?modifiedAt='
        pass

    def test_convo_single_friend_get(self):
        headers = get_headers()
        convo_id = get_convo_id()
        url = 'http://test.monkey.cool/api/v2/conversations/conversations/' + convo_id
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(result['conversation_id'], convo_id)

    def test_convo_send_msg_post(self):
        headers = get_headers()
        convo_id = get_convo_id()
        send_id = get_me_id()
        url = 'http://test.monkey.cool/api/v2/friendships/conversations/' + convo_id + '/message'
        payload = {'id': '53478055-2892-4bb5-b06b-991d97040c1b',
                   'type': 1,
                   'sender_id': send_id,
                   'content': 'This is test msg',
                   'extras': {},
                   'conversation_id': convo_id}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result['result'])
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    def test_convo_read_msg_post(self):
        headers = get_headers()
        convo_id = get_convo_id()
        url = 'http://test.monkey.cool/api/v2/friendships/conversations/' + convo_id +'/read'
        r = requests.post(url, headers=headers)
        '''
        # 注释此部分
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        current_timestamp = time.time()
        # print(current_time)
        # print(current_timestamp)
        read_timestamp_sec = result['data']['last_read_at']
        read_timestamp = read_timestamp_sec / 1000
        print(read_timestamp)
        # date_array = datetime.datetime.utcfromtimestamp(read_timestamp)
        # read_time = date_array.strftime('%Y-%m-%d %H:%M:%S')
        time_array = time.localtime(read_timestamp)
        read_time = time.strftime('%Y-%m-%d %H:%M:%S', time_array)
        # print(read_time)
        # 注释此部分
        '''
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])
        # self.assertAlmostEqual(first, second)

    def test_convo_del_convo_post(self):
        # get the users id and change to list

        '''# 注释此post
        chat_user_id = get_users_ids()[1].split(',')
        url = 'http://test.monkey.cool/api/v2/conversations/conversations/' + chat_user_id[1]
        print(url)
        r = requests.post(url, headers=headers)
        result = r.json()
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])
        # 注释此post'''

    @unittest.skip('to be tested later')
    def test_convo_recent_get(self):
        # url = '/api/v2/conversations/recent?updatedAtOpen={updatedAt}&updatedAtCollapsing={updatedAt}&loadOpen=true&loadCollapsing=true&type=1'
        pass

    def test_convo_question_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/conversations/questions'
        r = requests.get(url, headers=headers)
        statuscode = r.status_code
        result = r.json()
        # print(result)
        data = result['data']
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)

    @unittest.skip('to be modified')
    def test_convo_mod_status_unpair_post(self):
        headers = get_headers()
        chat_user_id_pair = get_users_ids()[4]
        if chat_user_id_pair == '':
            print('pair users are:%s' % chat_user_id_pair)
        else:
            chat_user_id_unpair = chat_user_id_pair.split(',')
            url = 'http://test.monkey.cool/api/v2/conversations/' + chat_user_id_unpair[-1] + '/status/6'
            r = requests.post(url, headers=headers)
            result = r.json()
            print(result)
            statuscode = r.status_code
            self.assertEqual(200, statuscode)

    def test_convo_mod_status_open_post(self):
        headers = get_headers()
        chat_user_id_collap = get_users_ids()[2]
        print(chat_user_id_collap)
        if chat_user_id_collap == '':
            print('open users are:%s' % chat_user_id_collap)
        else:
            chat_user_id_open = chat_user_id_collap.split(',')
            # print(chat_user_id_open)
            url = 'http://test.monkey.cool/api/v2/conversations/' + chat_user_id_open[-1] + '/status/1'
            r = requests.post(url, headers=headers)
            result = r.json()
            print(result)
            statuscode = r.status_code
            self.assertEqual(200, statuscode)
            self.assertEqual(1, result['status'])

    def test_convo_monkey_chat_get(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/conversations/monkeychattips'
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        data = result['data']
        self.assertEqual(200, statuscode)
        self.assertIsNotNone(data)

    def test_convo_check_msg_post(self):
        headers = get_headers()
        url = 'http://test.monkey.cool/api/v2/conversations/checkmessages'
        send_id = get_me_id()
        payload = {'send_id': send_id,
                   'receiver_id': 5266030,
                   'word': 'hahahah',
                   'check_type': 1}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        # dont assert status=0
        self.assertEqual(1, result['result'])

    def test_convo_specialf_get(self):
        headers = get_headers()
        friends_str = get_convo_id()
        # print(friends_str)
        friends = friends_str.split(':')
        friends_ids = ','.join(friends)
        # print(friends_ids)
        url = 'http://test.monkey.cool/api/v2/conversations/friends?ids=' + friends_ids
        # print(url)
        r = requests.get(url, headers=headers)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        data = result['data']
        self.assertEqual(200, statuscode)
        # print(data[0]['friendship_id'])
        self.assertEqual(data[0]['friendship_id'], friends_str)

    def test_convo_singlef_get(self):
        headers = get_headers()
        friendid = get_users_ids()[1].split(',')
        # print(friendid)
        url = 'http://test.monkey.cool/api/v2/conversations/friends/' + friendid[1]
        # print(url)
        r = requests.get(url, headers=headers)
        # result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)

    def test_chat_normal_check_post(self):
        headers = get_headers()
        send_id = get_me_id()
        receiver_id = get_senchat_user()[0]
        url = 'http://test.monkey.cool/api/v2/chat/sensitiveword'
        payload = {'sender_id': send_id,
                   'receiver_id': receiver_id,
                   'word': 'This is sensitive test',
                   'check_type': 1}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(1, result['result'])

    def test_chat_sensitive_check_post(self):
        headers = get_headers()
        send_id = get_me_id()
        receiver_id = get_senchat_user()[1]
        url = 'http://test.monkey.cool/api/v2/chat/sensitiveword'
        payload = {'sender_id': send_id,
                   'receiver_id': receiver_id,
                   'word': 'This is dick sensitive test',
                   'check_type': 1}
        r = requests.post(url, headers=headers, json=payload)
        result = r.json()
        # print(result)
        statuscode = r.status_code
        self.assertEqual(200, statuscode)
        self.assertEqual(0, result['result'])

    @unittest.skip('have removed categories')
    def test_chat_videocall_post(self):
        '''
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
        '''
        pass

if __name__ == '__main__':
    unittest.main()
