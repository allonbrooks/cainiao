#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 21:08
# @Author  : HandSome
# @File    : 如何找出数组中出现奇数次的数.py

def get2Num(arr):
	if arr ==None or len(arr) ==1:
		print('valid arr')
		return
	dic = dict()
	for i in range(len(arr)):
		if arr[i] not in dic:
			dic[arr[i]] =1
		else:
			dic[arr[i]] = 0
	return [k for k,v in dic.items() if v ==1]
