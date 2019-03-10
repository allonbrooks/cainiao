#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 10:46
# @Author  : HandSome
# @File    : 创建一个电话号码.py
"""
编写一个接受10个整数（0到9之间）数组的函数，它以电话号码的形式返回这些数字的字符串。

例如：

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def create_phone_numbers(arr):
	arr_to_str = ''.join([str(item) for item in arr])
	phone_number = '('+arr_to_str[:3]+') '+arr_to_str[3:6]+'-'+arr_to_str[6:]
	return phone_number

# 学习了新方法
def create_phone_numbers1(arr):
	return '({}{}{}) {}{}{}-{}{}{}{}'.format(*arr)

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

if __name__ == '__main__':
    verify.assert_equals(create_phone_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    verify.assert_equals(create_phone_numbers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
    verify.assert_equals(create_phone_numbers([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
    print(create_phone_numbers1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))