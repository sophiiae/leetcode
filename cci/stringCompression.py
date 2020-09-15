# perform basic string compression using the counts of repeated characters. 
# e.g. "aabcccccaaa" => "a2b1c5a3"
# if compressed string is not smaller, return original string. 
# Assume string has only uppercase or lowercase letters. 

def stringCompression (s: str):
	# time complexity: O(n), space complexity: O(1), but string is immutable, keep getting a new string
	if (len(s) < 3):
		return s
	chIndex = 0
	result = s[chIndex]
	for j in range(1, len(s)):
		if (s[j] != s[chIndex]):
			result += str(j - chIndex)
			chIndex = j
			result += s[chIndex]
		elif (j == len(s) - 1):
			result += str(j - chIndex + 1)
	if (len(result) >= len(s)):
		return s
	return result

print(stringCompression('aabcccccaaa'))
print(stringCompression('sssSSSwjeiiirrwlekk'))
print(stringCompression('abcderowlks'))
print(stringCompression('aa'))
print(stringCompression('ab'))
print(stringCompression('aaa'))
