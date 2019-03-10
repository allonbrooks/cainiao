
"""
编写一个函数，该函数将返回在输入字符串中出现多次(不同的不区分大小写的)字母字符和数字的计数。可以假定输入字符串仅包含字母（大写和小写）和数字。

例如:
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""
class verify:
	@staticmethod
	def assert_equals(fun,res):
		assert fun == res,'error'
		
def duplicate_count(text):
	dic = {}
	for item in text:
		if not dic.get(item.lower()):
			dic[item.lower()] = 1
		else:
			dic[item.lower()] += 1
	counts = len([item for item in list(dic.values()) if item > 1])
	return counts

def duplicate_count1(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

if __name__ == '__main__':
	verify.assert_equals(duplicate_count("abcde" ),0)
	verify.assert_equals(duplicate_count("aabbcde"), 2)
	verify.assert_equals(duplicate_count("aabBcde"), 2)
	verify.assert_equals(duplicate_count("indivisibility"), 1)
	verify.assert_equals(duplicate_count("Indivisibilities"), 2)
	verify.assert_equals(duplicate_count("aA11"), 2)
	verify.assert_equals(duplicate_count("ABBA"),2)