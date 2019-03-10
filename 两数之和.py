#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 11:36
# @Author  : HandSome
# @File    : 两数之和.py

def twosum(arr,target):
	dict = {}
	index = 0
	for i in range(len(arr)):
		if target - arr[i] in dict:
			return [dict[target - arr[i]],i]
		else:
			dict[arr[i]] = index
			index += 1
	
			
		
print(sum([1,2,4,7],9))



