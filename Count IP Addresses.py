#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 12:47
# @Author  : HandSome
# @File    : Count IP Addresses.py
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def iptoint(num):
	h=[]
	s = num.split(".")
	for temp in s:
		a = bin(int(temp))[2:]
		a = a.zfill(8)
		h.append(a)
		g = "".join(h)
	e = int(g,2)
	return e

def ips_between(start, end):
	return  iptoint(end) - iptoint(start)

if __name__ == '__main__':
	verify.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
	verify.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)