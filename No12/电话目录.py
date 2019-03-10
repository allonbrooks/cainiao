#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 11:11
# @Author  : HandSome
# @File    : 电话目录.py
'''
#2019刷题No12
刷题站 终极一题 这题会很难，毕竟最后一题！

1.电话目录

约翰将他的旧个人电话簿备份为文本文件。在文件中的每一行，他能找到的电话号码（如格式化+X-abc-def-ghij其中X代表一个或两个数字），与相应的名称&lt;，并&gt;和地址。

不幸的是，一切都是混合的，事情并不总是在同一个顺序; 线条的一部分混杂着非字母数字字符（电话号码和姓名除外）。

John的电话簿行示例：
"/+1-541-754-3010 156 Alphand_St. &lt;J Steeve&gt;\n"
" 133, Green, Rd. &lt;E Kustur&gt; NY-56423 ;+1-541-914-3010!\n"
"&lt;Anastasia&gt; +48-421-674-8974 Via Quirinal Roma\n"

你能帮助约翰做一个程序吗，根据他的电话簿和电话号码的行，返回一个这个数字的字符串： "Phone =&gt; num, Name =&gt; name, Address =&gt; adress"

例子：

s = "/+1-541-754-3010 156 Alphand_St. &lt;J Steeve&gt;\n 133, Green, Rd. &lt;E Kustur&gt; NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone =&gt; 1-541-754-3010, Name =&gt; J Steeve, Address =&gt; 156 Alphand St."


由于这道题的测试用例非常复杂，我把link贴出来，大家可以登入看一下测试用例



不到山穷水尽 不要看别人的答案
https://www.codewars.com/kata/phone-directory

'''

from re import sub

def phone1(dir, num):
	if dir.count("+" + num) == 0:
		return "Error => Not found: " + num
	
	if dir.count("+" + num) > 1:
		return "Error => Too many people: " + num
	
	for line in dir.splitlines():
		if "+" + num in line:
			name = sub(".*<(.*)>.*", "\g<1>", line)
			line = sub("<" + name + ">|\+" + num, "", line)
			address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
			return "Phone => %s, Name => %s, Address => %s" % (num, name, address)
import  re
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def phone(actual, num):
	if actual.count('+' + num) == 0:
		return 'Error => Not found: {}'.format(num)
	if actual.count('+' + num) > 1:
		return 'Error => Too many people: {}'.format(num)
	for items in actual.splitlines():
		if '+' + num in items:
			name = re.search('<(.*?)>', items).group(1)
			address = ' '.join(
				[item.strip() for item in items.replace(re.search('<(.*?)>', items).group(0), '').split()
				 if num not in item])
			address = re.sub(';|/|,', '', address)
			address = address.replace('_', "") if address[0] == '_' else address.replace('_', " ")
	return "Phone => {}, Name => {}, Address => {}".format(num, name, address)

if __name__ == '__main__':
	dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
		  "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
		  "+1-098-512-2222 <Peter Reedgrave>  Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
		  "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
		  "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
		  "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
		  "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
		  "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
		  "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
		  "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n")

	verify.assert_equals(phone(dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
	verify.assert_equals(phone(dr, "1-921-512-2222"), "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
	verify.assert_equals(phone(dr, "1-908-512-2222"), "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
	verify.assert_equals(phone(dr, "1-541-754-3010"), "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
	verify.assert_equals(phone(dr, "1-121-504-8974"), "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
	verify.assert_equals(phone(dr, "1-498-512-2222"), "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
	verify.assert_equals(phone(dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222")
	verify.assert_equals(phone(dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555")
