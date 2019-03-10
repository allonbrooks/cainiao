#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:12
# @Author  : HandSome
# @File    : 2.点赞.py
"""
你可能知道Facebook和其他网页上的“点赞”系统。人们可以“喜欢”博客文章，图片或其他项目。我们想要创建应该在这样的项目旁边显示的文本。

实现一个函数likes :: [String] -> String，它必须包含输入数组，包含喜欢项目的人的名字。它必须返回显示文本，如示例所示：
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
对于4个或更多名称，数字and 2 others只会增加。
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def moments(nameList):
	if len(nameList) == 0:
		output = 'no one likes this'
	elif len(nameList) == 1:
		output = '{} likes this'.format(nameList[0])
	elif len(nameList) == 2:
		output = '{} and {} like this'.format(nameList[0],nameList[1])
	elif len(nameList) == 3:
		output = '{}, {} and {} like this'.format(nameList[0],nameList[1],nameList[2])
	else:
		output = '{}, {} and {} others like this'.format(nameList[0],nameList[1],str(len(nameList)-2))
	return output

#方法二
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

if __name__ == '__main__':
	verify.assert_equals(moments(["Alex", "Jacob", "Mark", "Max"]),"Alex, Jacob and 2 others like this")
	verify.assert_equals(moments(["Max", "John", "Mark"]), "Max, John and Mark like this")
	verify.assert_equals(moments(["Jacob", "Alex"] ), "Jacob and Alex like this")
	verify.assert_equals(moments(["Peter"]), "Peter likes this")
	verify.assert_equals(moments( []), "no one likes this")