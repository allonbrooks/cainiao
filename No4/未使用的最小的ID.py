#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 11:00
# @Author  : HandSome
# @File    : 未使用的最小的ID.py
'''
你需要管理大量数据，使用零基础和非负ID来使每个数据项都是唯一的！
因此，需要一个方法来计算下一个新数据项返回最小的未使用ID...
注意：给定的已使用ID数组可能未排序。出于测试原因，可能存在重复的ID，但你无需查找或删除它们！
def next_id(arr):
    #your code here

测试用例：
verify.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
verify.assert_equals(next_id([5,4,3,2,1]), 0)
verify.assert_equals(next_id([0,1,2,3,5]), 4)
verify.assert_equals(next_id([0,0,0,0,0,0]), 1)
verify.assert_equals(next_id([]), 0)
'''
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
# 方法一
def next_id(arr):
	t = 0
	while t in arr:
		t += 1
	return t


if __name__ == '__main__':
	verify.assert_equals(next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)
	verify.assert_equals(next_id([5, 4, 3, 2, 1]), 0)
	verify.assert_equals(next_id([0, 1, 2, 3, 5]), 4)
	verify.assert_equals(next_id([0, 0, 0, 0, 0, 0]), 1)
	verify.assert_equals(next_id([]), 0)
	verify.assert_equals(next_id([0, 0, 1, 1, 2, 2]), 3)
