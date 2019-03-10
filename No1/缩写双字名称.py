#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 11:44
# @Author  : HandSome
# @File    : 缩写双字名称.py
def abbrevName(name):
	
	trans_name = '.'.join([item.upper()[0] for item in name.split(' ')])
	return trans_name
if __name__ == '__main__':
 
	name = 'P Favuzzzi'
	trans_name = '.'.join([item.upper()[0] for item in name.split(' ')])
	print(trans_name)

