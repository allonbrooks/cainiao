#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:44
# @Author  : HandSome
# @File    : 检查信用卡.py

"""
给定一个信用卡号码，我们可以通过一些基本知识来确定发行人/供应商是谁。

完成get_issuer()将使用下面显示的值的功能来确定给定卡号的发卡机构。如果数字不匹配，则该函数应返回该字符串Unknown。

  Card Type     Begins With             Number Length
  AMEX          34 or 37                15
  Discover      6011                    16
  Mastercard    51, 52, 53, 54 or 55    16
  VISA          4                       13 or 16
"""
def get_isuser(cardnumber):
	cardnumber = str(cardnumber)
	if cardnumber.startswith(('34','37')) and len(cardnumber) ==15:
		ueser = 'AMEX'
	elif  cardnumber.startswith('6011') and len(cardnumber) ==16:
		ueser = 'Discover'
	elif  cardnumber.startswith(('51','52','53','54','55')) and len(cardnumber) ==16:
		ueser = 'Mastercard'
	elif  cardnumber.startswith('4') and len(cardnumber) in [13,16]:
		ueser = 'VISA'
	else:
		ueser = 'Unknown'
	return ueser


if __name__ == '__main__':
	assert get_isuser(4111111111111111) == 'VISA','error'
	assert get_isuser(4111111111111) == 'VISA', 'error'
	assert get_isuser(4012888888881881) == 'VISA', 'error'
	assert get_isuser(378282246310005) == 'AMEX', 'error'
	assert get_isuser(6011111111111117) == 'Discover', 'error'
	assert get_isuser(5105105105105100) == 'Mastercard', 'error'
	assert get_isuser(5205105105105106) == 'Mastercard', 'error'
	assert get_isuser(9111111111111117) == 'Unknown', 'error'
	
	
	
	