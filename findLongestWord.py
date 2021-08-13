import collections

def findLongestWord(s: str, dictionary) -> str:
	dictionary.sort(key=lambda x:(-len(x), x))
	for word in dictionary:
		last = 0
		
		for char in word:
			last = s.find(char, last)+1
			if last==0:
				break
		else:
			return word
	return ""

s = "aewfafwafjlwajflwajflwafj"
d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]

print(findLongestWord(s, d))

e = ['b', 'x', 'a','g','bo','be']
print(e)
e.sort(key=lambda x: (-len(x), x))
print(e)
