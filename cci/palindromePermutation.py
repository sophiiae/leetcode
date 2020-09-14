# Given a string, check if it is a permutation of palindrome. 
# e.g. "Tact Coa" => True ('taco cat', 'atco cta", etc)
# Question: all letters? case senstive?

def palindromePermutation(s: str):
	# use ASCII index for characters
	table = [0] * (ord('z') - ord('a') + 1)
	for ch in s: 
		num = ord(ch.lower())
		# only count for letters
		if (num <= ord('z') and num >= ord('a')):
			table[num - ord('a')] += 1
	
	quota = 1 #palindrome can have at most one odd letter
	for count in table:
		if (count % 2): #odd
			if (quota == 0):
				return False
			else:
				quota -= 1
	return True

print(palindromePermutation('Tact Coa'))
print(palindromePermutation('aadjjeiie'))
print(palindromePermutation('pale, ale'))
print(palindromePermutation('dweuwj, eu'))
