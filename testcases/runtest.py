# -*- coding:utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time


# report_path = os.path.abspath(os.path.dirname(__file__))
report_path = os.path.dirname(os.getcwd())

# test_dir = 'D:\\Monkeyapi\\testcases'
test_dir = os.path.abspath(os.path.dirname(__file__))
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = report_path + '\\test_report\\' + now + 'test_result.html'
    # filename = 'D:\\Monkeyapi' + '\\test_report\\' + now + 'test_result.html'
    # print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='MonkeyApiTestReport:',
                            description='Monkeyapitestresult')
    runner.run(discover)
    fp.close()
