#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 10:18
# @Author  : HandSome
# @File    : 2.拼接字符.py

'''
根据下面的表达式设计一个函数:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''
def accum(strs):
	
	new_strs = '-'.join([str(item * (i+1)).capitalize() for i,item in enumerate(strs)])
	return new_strs

if __name__ == '__main__':
	assert accum("abcd") == 'A-Bb-Ccc-Dddd','error'
	assert accum('RqaEzty') == 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy','error'
	assert accum("cwAt") == 'C-Ww-Aaa-Tttt','error'
	