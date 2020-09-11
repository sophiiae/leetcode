def isUnique(s: str):
	table = {}
	for ch in s: 
		if (ch in table):
			return False
		else:
			table[ch] = 1
	return True

def isUniqueChars(s: str):
	if (len(s) > 128):
		return False
	
	asciiArr = [False] * 128
	for ch in s:
		if (asciiArr[ord(ch)]):
			return False
		else:
			asciiArr[ord(ch)] = True
	return True


print(isUnique("abcdefg"))
print(isUnique("kk"))
print(isUnique("asdfg.hjk*&^3%4ld#iueq"))

print(isUniqueChars("abcdefg"))
print(isUniqueChars("kk"))
print(isUniqueChars("asdfg.hjk*&^3%4ld#iueq"))
