#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 9:32
# @Author  : HandSome
# @File    : 1.来排个序.py

"""
你的任务是对给定的字符串进行排序。字符串中的每个单词都包含一个数字。此数字是单词在结果中应具有的位置。

注意：数字可以是1到9.因此1将是第一个单词（不是0）。

如果输入字符串为空，则返回空字符串。输入String中的单词只包含有效的连续数字。

例子:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""
import  re

class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def strSort(inputstr):
	new_str = ' '.join(sorted(inputstr.split(), key=lambda x:int(re.search('\d+',x).group())))
	return new_str

	
if __name__ == '__main__':
	verify.assert_equals(strSort('is2 Thi1s T4est 3a'), 'Thi1s is2 3a T4est')
	verify.assert_equals(strSort('4of Fo1r 2sum pe6ople g3ood th5e the20'), 'Fo1r 2sum g3ood 4of th5e pe6ople the20')
	verify.assert_equals(strSort(''), '')
