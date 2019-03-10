#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 20:28
# @Author  : HandSome
# @File    : 2.递归数字总和.py
"""
写一个函数叫digital_root,给定一个数字，递归遍历数字从个位，十位，百位...以此相加计算总和。则以这种方式继续减少，直到产生一位数字。这仅适用于自然数

比如:
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""


class verify:
	@staticmethod
	def assert_equals(fun, res):
		assert fun == res, 'error'

def digital_root(inputnumber):
	
	result = sum([int(item) for item in str(inputnumber)])
	return digital_root(result) if result > 9 else result
	
if __name__ == '__main__':
	verify.assert_equals(digital_root(493193), 2)
	verify.assert_equals(digital_root(16), 7)
	verify.assert_equals(digital_root(942), 6)
	verify.assert_equals(digital_root(132189), 6)
