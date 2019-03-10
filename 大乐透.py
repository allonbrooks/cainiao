#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 22:36
# @Author  : HandSome
# @File    : 大乐透.py

result = {}
for a in range(0,10):
	for b in range(0, 10):
		for c in range(0, 10):
			sum = a + b + c
			if not result.get(sum):
				result[sum] = 1
			else:
				result[sum] += 1
			
m = 0
for i in range(8, 20):
	m += result[i]
print(m)
# result = sorted(result.items(),key = lambda x:x[0])
print(result)

d = result[8]*19/1000 + result[9]*18/1000 +result[10]*16/1000 +result[11]*15/1000 + result[12]*14/1000 +result[13]*12/1000
print(d/6)