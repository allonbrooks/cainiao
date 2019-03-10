#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 9:29
# @Author  : HandSome
# @File    : 1.用函数计算.py
'''
这次我们想用函数编写计算并得到结果。我们来看看一些例子：

例如：
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
'''
#方法二
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
'''
值得学习的地方：
1、三元表达式，返回操作符的函数，并将当前参数传入
2、操作符函数使用了简洁的lambda表达式
3、lambda的写法还是挺难理解的，这里应该从里往外看，比如：eight(divided_by(four()))
应该先算出four()这个式子，然后再看divided_by(four())->lambda x: x/4 看得出来这个时候lambda还没有被调用
最后eight(operation)的时候，调用了当前的lambda 等效于 执行了 divided_by(4)(8)
'''
def zero(f=None): return 0 if not f else f(0)
def one(f=None): return 1 if not f else f(1)
def two(f=None): return 2 if not f else f(2)
def three(f=None): return 3 if not f else f(3)
def four(f=None): return 4 if not f else f(4)
def five(f=None): return 5 if not f else f(5)
def six(f=None): return 6 if not f else f(6)
def seven(f=None): return 7 if not f else f(7)
def eight(f=None): return 8 if not f else f(8)
def nine(f=None): return 9 if not f else f(9)
def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda  x: x/y

# #方法一
def zero(operation=None): return int(eval('0%s' % operation)) if operation else 0
def one(operation=None): return int(eval('1%s' % operation)) if operation else 1
def two(operation=None): return int(eval('2%s' % operation)) if operation else 2
def three(operation=None): return int(eval('3%s' % operation)) if operation else 3
def four(operation=None): return int(eval('4%s' % operation)) if operation else 4
def five(operation=None): return int(eval('5%s' % operation)) if operation else 5
def six(operation=None): return int(eval('6%s' % operation)) if operation else 6
def seven(operation=None): return int(eval('7%s' % operation)) if operation else 7
def eight(operation=None): return int(eval('8%s' % operation)) if operation else 8
def nine(operation=None): return int(eval('9%s' % operation)) if operation else 9
def plus(num): return '+%s' % num
def minus(num): return '-%s' % num
def times(num): return '*%s' % num
def divided_by(num):return '/%s' % num





if __name__ == '__main__':
	verify.assert_equals(seven(times(five())),35)
	verify.assert_equals(eight(minus(three())), 5)
	verify.assert_equals(four(plus(nine())), 13)
	verify.assert_equals(six(divided_by(two())), 3)
	