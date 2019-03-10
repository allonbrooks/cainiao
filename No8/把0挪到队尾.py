#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 19:45
# @Author  : HandSome
# @File    : 把0挪到队尾.py
"""
编写一个算法，该算法采用数组并将所有零移动到最后，保留其他元素的顺序。
例如：
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

测试用例：
verify.describe("Basic tests")
verify.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
verify.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
verify.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
verify.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
verify.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
verify.assert_equals(move_zeros(["a","b"]),["a","b"])
verify.assert_equals(move_zeros(["a"]),["a"])
verify.assert_equals(move_zeros([0,0]),[0,0])
verify.assert_equals(move_zeros([0]),[0])
verify.assert_equals(move_zeros([False]),[False])
verify.assert_equals(move_zeros([]),[])
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def move_zeros(array):
	
	l = [i for i in array if isinstance(i,bool) or i!=0]
	return l+[0]*(len(array)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

if __name__ == '__main__':
	verify.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
	verify.assert_equals(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
	                   [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	verify.assert_equals(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
	                   ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	verify.assert_equals(
		move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
		["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	verify.assert_equals(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
	verify.assert_equals(move_zeros(["a", "b"]), ["a", "b"])
	verify.assert_equals(move_zeros(["a"]), ["a"])
	verify.assert_equals(move_zeros([0, 0]), [0, 0])
	verify.assert_equals(move_zeros([0]), [0])
	verify.assert_equals(move_zeros([False]), [False])
	verify.assert_equals(move_zeros([]), [])