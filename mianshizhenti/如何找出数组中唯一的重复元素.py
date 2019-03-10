#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 20:34
# @Author  : HandSome
# @File    : 如何找出数组中唯一的重复元素.py

"""
【出自 BD 面试题】
难度系数：，传，传食
题目描述：
被考察系数：食食，传，传食
数字 1000 放在含有 1001 个元素的数组中，其中只有唯 个元素值重复，其他数
字均只出现 次。设计 个算法，将重复元素找出来，要求每个数组元素只能访问一次。如
果不使用辅助存储空间，能否设计一个算法实现？
"""
def findDup(array):
	if array == None:
		return -1
	lens = len(array)
	i  = 0
	result = 0
	while i < lens:
		result ^= array[i]
		i +=1
	j = 1
	while j < lens:
		result ^= j
		j += 1
	return result
if __name__ == '__main__':
	array = [1,3,4,2,5,3]
	print(findDup(array))