#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 20:55
# @Author  : HandSome
# @File    : python内存管理机制.py

import gc
import objgraph

class A(object):
	pass

class B(object):
	pass

def C():
	a= A()
	b = B()
	
C()
print(objgraph.count('A'))
print(objgraph.count('B'))