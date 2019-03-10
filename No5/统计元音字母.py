#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 9:56
# @Author  : HandSome
# @File    : 统计元音字母.py


"""
给一个字符串，统计里面的元音字母！我们给定的元音列表是:[a, e, i, o, u ] ,输入的字符串只会是小写字母或者含有空格。

代码:
def getCount(inputStr):
    num_vowels = 0
    # your code here
    
    return num_vowels

测试用例：
test.assert_equals(getCount("abracadabra"), 5)
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'

def getCount(inputStr):
	
	yuanyin = ['a', 'e', 'i', 'o', 'u' ]
	return len([item for item in inputStr if item in yuanyin ])

if __name__ == '__main__':
	verify.assert_equals(getCount("abracadabra"), 5)
	verify.assert_equals(getCount(""), 0)
	verify.assert_equals(getCount("abcd a"), 2)