#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 10:58
# @Author  : HandSome
# @File    : 1.反转一个数字.py

'''
给定一个数字，写一个函数来输出其反向数字。（例如，给出123答案是321）
数字应该保留他们的标志; 即反转时负数仍应为负数。
比如:
 123 ->  321
-456 -> -654
1000 ->    1
'''
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def reverse_number(inputnumber):
	new_str = str(inputnumber).rstrip('0')
	return int(new_str[::-1][:-1])*(-1) if "-" in new_str else int(new_str[::-1])

if __name__ == '__main__':
	verify.assert_equals(reverse_number(123),321)
	verify.assert_equals(reverse_number(-456), -654)
	verify.assert_equals(reverse_number(1000), 1)
	verify.assert_equals(reverse_number(-123), -321)
	verify.assert_equals(reverse_number(5), 5)
	verify.assert_equals(reverse_number(4321234), 4321234)
	verify.assert_equals(reverse_number(98989898), 89898989)
	