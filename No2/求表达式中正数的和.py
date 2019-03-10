#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 10:07
# @Author  : HandSome
# @File    : 求表达式中正数的和.py

"""
你得到一组数字，返回所有正数的总和。

示例[1,-4,7,12]=>1 + 7 + 12 = 20

注意：如果没有要求的总和，则默认值为0。
"""

def positive_sum(arr):
	
	positive_sum= sum([item if item >0 else 0 for item in arr])
	return positive_sum

if __name__ == '__main__':
	assert  positive_sum([]) == 0,'error'
	assert positive_sum([-1,-2,-4]) == 0,'error'
	assert positive_sum([1,-4,7,12]) == 20,'error'