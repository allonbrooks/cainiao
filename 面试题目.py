#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 13:41
# @Author  : HandSome
# @File    : 面试题目.py

def f1(lIn):
	l1 = sorted(lIn)
	l2 = [i for i in l1 if i<0.5]
	return [i*i for i in l2]
def f2(lIn):
	l1 = [i for i in lIn if i<0.5]
	l2 = sorted(l1)
	return [i*i for i in l2]
def f3(lIn):
	l1 = [i*i for i in lIn]
	l2 = sorted(l1)
	return [i for i in l2 if i<(0.5*0.5)]

import random
import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')