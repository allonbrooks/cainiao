#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 10:54
# @Author  : HandSome
# @File    : 3.py
"""
编写一个在1，2，…，9（顺序不能变）数字之间插入+或-或什么都不插入，使得计算结果总是100的程序，并输出所有的可能性。例如：1 + 2 + 34 – 5 + 67 – 8 + 9 = 100。
"""

str = '1{}2{}3{}4{}5{}6{}7{}8{}9'
odd = ["+","-",""]
for i1 in odd:
	for i2 in odd:
		for i3 in odd:
			for i4 in odd:
				for i5 in odd:
					for i6 in odd:
						for i7 in odd:
							for i8 in odd:
								str1 = str.format(i1,i2,i3,i4,i5,i6,i7,i8)
								if eval(str1) ==100:
									print(str1,"=100")
							

arr = [item for item in 'abcdefghijklmnopqrstuvwxyz']
arr_list = []
for  a in arr:
	for b in arr:
			for c in arr:
				if a!=b and b!=c:
					arr_list.append((a+b+c))
print(len(set(arr_list)))
print(arr_list)
