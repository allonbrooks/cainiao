#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 9:29
# @Author  : HandSome
# @File    : 2.我应该选择哪个加油站？.py
'''
你必须填满你的天然气，有多个加油站，价格和距离不同。有时候开车到更远的加油站会更便宜，因为价格更便宜！

- 你的汽车最多可以容纳60升。
- 你需要把你的汽车装满
- 根据加油站的实际价格计算油箱中的当前燃油

记住：你还需要燃料才能开到加油站！回家的路也应该考虑！

测试用例：
Test.describe("Default Tests")
obj = {"Powerfiller":{"price": 2, "distance": 50},
        "Powerfuel": {"price": 1.5, "distance": 75}}
currentFuel = 35
fuelConsumption = 7.5
Test.assert_equals(gas_station(obj, currentFuel, fuelConsumption), "Powerfuel")

obj = {"iFuel": {"price": 1.5, "distance": 50},
        "Tanker": {"price": 2.0, "distance": 75}}
currentFuel = 1
fuelConsumption = 7.5
Test.assert_equals(gas_station(obj, currentFuel, fuelConsumption), None)
'''
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def gas_stations(obj,currentFuel,fuelConsumption):
	Support_distance = currentFuel/(fuelConsumption/100)
	all_distance = [v["distance"]for k,v in obj.items()]
	if Support_distance < min(all_distance):
		return None
	else:
		for k,v in obj.items():
			if v['distance'] < Support_distance:
				addGasvolume = 60 - v['distance']*fuelConsumption/100#到油站需要添加多少油 = 回到家还有多少钱
				v['paste'] = addGasvolume*v['price']#添加满灌花费多少钱
		return sorted(obj.items(),key=lambda x:x[1]['paste'])[0][0]

if __name__ == '__main__':
	obj1 = {"iFuel": {"price": 1.5, "distance": 50},
	       "Tanker": {"price": 2.0, "distance": 75}}
	currentFuel1 = 1
	fuelConsumption1 = 7.5
	verify.assert_equals(gas_stations(obj1, currentFuel1, fuelConsumption1),None)
	obj = {"Powerfiller": {"price": 2, "distance": 50},
	       "Powerfuel": {"price": 1.5, "distance": 75}}
	currentFuel = 35
	fuelConsumption = 7.5
	verify.assert_equals(gas_stations(obj, currentFuel, fuelConsumption), 'Powerfuel')