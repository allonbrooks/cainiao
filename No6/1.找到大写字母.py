#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 20:24
# @Author  : HandSome
# @File    : 1.找到大写字母.py

"""
写一个函数capitals()给你一串字符串，找到里面的大写字母，并返回它们的index.

比如：
capitals('CodEWaRs')输出为 [0,3,4,6]
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'

def capitals(inpustr):
	return [index for index,values in enumerate(inpustr) if values.isupper()]

if __name__ == '__main__':
	verify.assert_equals(capitals('CodEWaRs'),[0,3,4,6])