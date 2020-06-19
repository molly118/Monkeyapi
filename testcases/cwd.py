# -*- coding:utf-8 -*-
import os

report_path = os.path.abspath(os.path.dirname(__file__))
'''
print(report_path)  # D:\Monkeyapi\testcases
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))  # D:\
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # D:\Monkeyapi\testcases
print(os.path.abspath(os.path.join(os.getcwd(), "..")))  # D:\Monkeyapi
print(os.path.abspath(os.path.dirname(os.getcwd()))) # D:\Monkeyapi
print(os.path.dirname(os.getcwd())) # D:\Monkeyapi
'''
print(os.getcwd())# D:\Monkeyapi\testcases

'''
import os

print '***获取当前目录***'
print os.getcwd()
print os.path.abspath(os.path.dirname(__file__))

print '***获取上级目录***'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))

print '***获取上上级目录***'
print os.path.abspath(os.path.join(os.getcwd(), "../.."))
--------------------------------------------------------- 
'''
