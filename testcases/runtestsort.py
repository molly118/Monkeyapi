import sys
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time
from test_follow import TestFollow, TestBlockReport, TestHmu
from test_config import TestConfig
from test_moment import TestMoment
from test_msg import TestMsg
from test_user import TestUserInfo

reload(sys)
sys.setdefaultencoding('utf8')


# report_path = os.path.abspath(os.path.dirname(__file__))
report_path = os.path.dirname(os.getcwd())

# test_dir = 'D:\\Monkeyapi\\testcases'
test_dir = os.path.abspath(os.path.dirname(__file__))

# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
4

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestFollow('test_follow_origin_post'))
    suite.addTest(TestFollow('test_unfollow_post'))
    suite.addTest(TestFollow('test_follow_none_origin_post'))
    suite.addTest(TestFollow('test_ignore_follow_get'))
    suite.addTest(TestFollow('test_following_list_get'))
    suite.addTest(TestFollow('test_follower_list_get'))
    suite.addTest(TestFollow('test_search_user_post'))
    suite.addTest(TestFollow('test_follow_request_get'))
    suite.addTest(TestBlockReport('test_block_post'))
    suite.addTest(TestBlockReport('test_unblock_post'))
    suite.addTest(TestBlockReport('test_blocklist_get'))
    suite.addTest(TestBlockReport('test_report_otherprofile_post'))
    suite.addTest(TestHmu('test_click_hmu_post'))
    suite.addTest(TestHmu('test_hmu_list_get'))
    suite.addTest(TestConfig('test_config_filters_get'))
    suite.addTest(TestConfig('test_config_get'))
    suite.addTest(TestConfig('test_config_story_get'))
    suite.addTest(TestConfig('test_config_servertime_get'))
    suite.addTest(TestConfig('test_config_famous_get'))
    suite.addTest(TestMoment('test_moment_category_get'))
    suite.addTest(TestMoment('test_moment_category_list_get'))
    suite.addTest(TestMoment('test_moment_watched_post'))
    suite.addTest(TestMoment('test_moment_like_post'))
    suite.addTest(TestMoment('test_moment_cate_info_get'))
    suite.addTest(TestMoment('test_moment_one_info_get'))
    suite.addTest(TestMoment('test_moment_send_dm_post'))
    suite.addTest(TestMoment('test_moment_list_sb_get'))
    suite.addTest(TestMoment('test_moment_likeuser_list_get'))
    suite.addTest(TestMoment('test_moment_report_post'))
    suite.addTest(TestMoment('test_moment_info_me_get'))
    suite.addTest(TestMoment('test_moment_answer_post'))
    suite.addTest(TestMoment('test_moment_sb_recent_get'))
    suite.addTest(TestMoment('test_moment_nearby_get'))
    suite.addTest(TestMoment('test_moment_infos_get'))
    suite.addTest(TestMoment('test_moment_send_ama_post'))
    suite.addTest(TestMsg('test_user_dm_default_post'))
    suite.addTest(TestMsg('test_user_dm_recent_post'))
    suite.addTest(TestMsg('test_story_dm_post'))
    suite.addTest(TestMsg('test_convo_friends_get'))
    suite.addTest(TestMsg('test_convo_single_friend_get'))
    suite.addTest(TestMsg('test_convo_send_msg_post'))
    suite.addTest(TestMsg('test_convo_read_msg_post'))
    suite.addTest(TestMsg('test_convo_del_convo_post'))
    suite.addTest(TestMsg('test_convo_recent_get'))
    suite.addTest(TestMsg('test_convo_question_get'))
    suite.addTest(TestMsg('test_convo_mod_status_unpair_post'))
    suite.addTest(TestMsg('test_convo_mod_status_open_post'))
    suite.addTest(TestMsg('test_convo_monkey_chat_get'))
    suite.addTest(TestMsg('test_convo_check_msg_post'))
    suite.addTest(TestMsg('test_convo_specialf_get'))
    suite.addTest(TestMsg('test_convo_singlef_get'))
    suite.addTest(TestMsg('test_chat_normal_check_post'))
    suite.addTest(TestMsg('test_chat_sensitive_check_post'))
    suite.addTest(TestMsg('test_chat_videocall_post'))
    suite.addTest(TestUserInfo('test_me_info_get'))
    suite.addTest(TestUserInfo('test_one_user_info_get'))
    suite.addTest(TestUserInfo('test_more_users_infos_get'))

    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = report_path + '\\test_report\\' + now + 'test_result.html'
    # filename = 'D:\\Monkeyapi' + '\\test_report\\' + now + 'test_result.html'
    # print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='MonkeyApiTestReport:',
                            description='Monkeyapitestresult')
    runner.run(suite)
    fp.close()
