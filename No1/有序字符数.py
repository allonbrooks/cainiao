#方法一
def ordered_count(strs):
	resluts = []
	for item in strs:
		counts= (item, strs.count(item))
		if counts not in resluts:
			resluts.append(counts)
	return  resluts
#方法二
def ordered_count__(strs):
	resluts = []
	set_strs = list(set(strs))
	set_strs.sort(key=strs.index)
	for item in set_strs:
		resluts.append((item, strs.count(item)))
	return resluts
if __name__ == '__main__':
	strs1= 'Code Wars'
	strs2 = 'abracadabra'
	ordered_count1 = ordered_count(strs1)
	ordered_count2 = ordered_count(strs2)
	print('ordered_count("' + strs1 + '")==', ordered_count1)
	print('ordered_count("' + strs2 + '")==', ordered_count2)
	print(ordered_count__(strs2))
