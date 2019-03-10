#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:03
# @Author  : HandSome
# @File    : 人性化的可读性时间.py
"""
编写一个函数，它以非负整数（秒）作为输入，并以人类可读的格式返回时间（HH:MM:SS）

- HH =小时，填充到2位数，范围：00 - 99
- MM =分钟，填充到2位数，范围：00 - 59
- SS =秒，填充到2位数，范围：00 - 59

最长时间永远不会超过359999（99:59:59）
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def  make_readable(inputnumber):
	if inputnumber <= 359999:
		m, s = divmod(inputnumber, 60)
		h, m = divmod(m, 60)
		time = "%02d:%02d:%02d" % (h, m, s)
		return time
	else:
		return None
if __name__ == '__main__':
	verify.assert_equals(make_readable(0),'00:00:00')
	verify.assert_equals(make_readable(5), '00:00:05')
	verify.assert_equals(make_readable(60), '00:01:00')
	verify.assert_equals(make_readable(86399), '23:59:59')
	verify.assert_equals(make_readable(359999), '99:59:59')
	verify.assert_equals(make_readable(39999999999), None)
	