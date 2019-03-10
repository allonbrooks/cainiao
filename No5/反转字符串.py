#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 10:01
# @Author  : HandSome
# @File    : 反转字符串.py

"""
编写一个函数，它接受一个或多个单词的字符串，其中里面含五个或更多字母单词必须要反转。传入的字符串只包含字母和空格。仅当存在多个单词时才会包含空格。

比如:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

测试用例：
test.assert_equals(spin_words("Welcome"), "emocleW")
"""

class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def spin_words(inputstr):
	
	return " ".join([item[::-1] if len(item) >=5 else item for item in inputstr.split(" ")])

if __name__ == '__main__':
	verify.assert_equals(spin_words("Welcome"), "emocleW")
	verify.assert_equals(spin_words("Hey fellow warriors") ,"Hey wollef sroirraw")
	verify.assert_equals(spin_words("This is a test"),"This is a test")
	verify.assert_equals(spin_words("This is another test"),"This is rehtona test")
	