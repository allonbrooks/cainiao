#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 10:25
# @Author  : HandSome
# @File    : 1.py

"""
使用for循环、while循环和递归写出3个函数来计算给定数列的总和。
"""
def get_sum(arr):
	sum = 0
	for item in arr:
		sum +=item
	return sum

def get_sum1(arr):
	sum = 0
	i = 0
	while i < len(arr):
		sum += arr[i]
		i +=1
	return sum

def get_sum3(arr):
	if arr == []:
		return 0
	return arr[0] +get_sum3(arr[1:])

if __name__ == '__main__':
	print(get_sum([1, 2, 3, 4]))
	print(get_sum1([1, 2, 3, 4]))
	print(get_sum3([1, 2, 3, 4,5]))