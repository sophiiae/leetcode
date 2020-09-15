# insert, replace, remove
# check if a string is one edit or zero edit away from the other

def oneEditAway(s1: str, s2: str):
	if (len(s1) - len(s2) > 1 or len(s2) - len(s1) > 1):
		return False
	
	table = {}
	for ch in s1:
		if (ch in table):
			table[ch] += 1
		else:
			table[ch] = 1
	insert = 1
	for ch in s2:
		if ch in table:
			if (table[ch] == 1):
				del table[ch]
			else:
				table[ch] -= 1
		else:
			if (insert == 0):
				return False
			else:
				insert -= 1
	if (len(table) > 1):
		return False
	return True

print(oneEditAway('pale', 'ple')) #True
print(oneEditAway('pales', 'pale')) #True
print(oneEditAway('pale', 'bale')) #True
print(oneEditAway('pale', 'bake')) #False
print(oneEditAway('pales', 'pes')) #False