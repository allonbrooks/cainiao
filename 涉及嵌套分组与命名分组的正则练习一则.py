#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 22t:02
# @Author  : HandSome
# @File    : 涉及嵌套分组与命名分组的正则练习一则.py

"""
有文本若干行如下，请写出正则匹配出以 param 开头的参数信息，输出格式为：字段名称、字段类型（不带尖括号）、是否可选（不带尖括号）和字段含义四部分内容。

#param  nickname    <str>    昵称
#param  sex    <int>    <可选>    学员性别，1 男，2 女
"""

import re

text = '''
#param  nickname    <str>    昵称
#param  sex    <int>    <可选>    学员性别，1 男，2 女
'''
import re

text = """
#param  nickname    <str>    昵称
#param  sex    <int>    <可选>    学员性别，1 男，2 女
"""

# 使用命名分组
p = re.compile(r'#param\s+(?P<name>[a-zA-Z]+)\s+<(?P<type>[a-zA-Z]+)>(\s+<(?P<opt>.+)>)?\s+(?P<desc>.+)')
result = p.finditer(text)
for i in result:
    print(i.group('name', 'type', 'opt', 'desc'))
