#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:37
# @Author  : HandSome
# @File    : 判断奇数还是偶数.py

class test:
	@staticmethod
	def expect(fun,res):
		assert fun ==res,'error'
		
def even_or_odd(number):
	return "Even" if abs(number)%2 == 0 else 'Odd'

if __name__ == '__main__':
	test.expect(even_or_odd(2),"Even")
	test.expect(even_or_odd(0), "Even")
	test.expect(even_or_odd(7), "Odd")
	test.expect(even_or_odd(1), "Odd")
	test.expect(even_or_odd(-1), "Odd")
	test.expect(even_or_odd(-4), "Even")
	