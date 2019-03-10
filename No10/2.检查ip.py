#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 11:17
# @Author  : HandSome
# @File    : 2.检查ip.py

'''
编写一种算法，以十进制格式识别有效的IPv4地址。如果IP由四个八位字节组成，其值在0和之间255，则应视为有效。
该函数的输入保证是单个字符串。
例子：有效输入
1.2.3.4
123.45.67.89

无效输入：
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
'''
import re
from collections import Counter
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def is_valid_IP(hostip):
	ip_list = hostip.split('.')
	if len(ip_list) != 4:
		return False
	else:
		for item in ip_list:
			if not item.isdigit() or (item.startswith('0') and len(item) >1):
				return False
			i = int(item)
			if i <0 or i >255:
				return False
		return True

if __name__ == '__main__':
	verify.assert_equals(is_valid_IP('12.255.56.1'), True)
	verify.assert_equals(is_valid_IP(''), False)
	verify.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
	verify.assert_equals(is_valid_IP('123.456.789.0'), False)
	verify.assert_equals(is_valid_IP('12.34.56'), False)
	verify.assert_equals(is_valid_IP('12.34.56 .1'), False)
	verify.assert_equals(is_valid_IP('12.34.56.-1'), False)
	verify.assert_equals(is_valid_IP('123.045.067.089'), False)
	verify.assert_equals(is_valid_IP('127.1.1.0'), True)
	verify.assert_equals(is_valid_IP('0.0.0.0'), True)
	verify.assert_equals(is_valid_IP('0.34.82.53'), True)
	verify.assert_equals(is_valid_IP('192.168.1.300'), False)

	

		
	