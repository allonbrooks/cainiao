#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 11:20
# @Author  : HandSome
# @File    : 获得中间字符.py

"""
你会得到一个字符串,你需要写一个函数返回单词的中间字符。如果单词的长度为奇数，则返回中间字符。如果单词的长度是偶数，则返回中间2个字符。

例如：
Kata.get_middle("verify") should return "ri"
Kata.get_middle("testing") should return "t"
Kata.get_middle("middle") should return "dd"
Kata.get_middle("A") should return "A"
测试用例：
verify.assert_equals(get_middle("verify"),"ri")
verify.assert_equals(get_middle("testing"),"t")
verify.assert_equals(get_middle("middle"),"dd")
verify.assert_equals(get_middle("A"),"A")
verify.assert_equals(get_middle("of"),"of")
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def get_middle(s):
	index, odd = divmod(len(s), 2)
	return s[index] if odd else s[index - 1:index + 1]
	
verify.assert_equals(get_middle("verify"),"ri")
verify.assert_equals(get_middle("testing"),"t")
verify.assert_equals(get_middle("middle"),"dd")
verify.assert_equals(get_middle("A"),"A")
verify.assert_equals(get_middle("BA"),"BA")
verify.assert_equals(get_middle(""),"")

