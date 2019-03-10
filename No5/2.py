#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 10:45
# @Author  : HandSome
# @File    : 2.py

"""
编写一个能将给定非负整数列表中的数字排列成最大数字的函数。例如，给定[50，2，1,9]，最大数字为95021。
"""
def big_number(lst):
    lst = [str(i) for i in lst]
    print(lst)
    lst = sorted(lst,reverse=True)
    print(lst)
    return int(''.join(lst))
if __name__ == '__main__':
    lst = [50,2,1,4]
    print(big_number(lst))
