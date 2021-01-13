# replace all space with '%20', may assume there are space at the end. The true length of the str is given. 
# e.g. "Mr John Smith             ", 13  => "Mr%20John%20Smith"

def urlify(s: str, truelength: int):
	url, index = '', 0
	while (index < truelength):
		if (s[index] == ' '):
			url += '%20'
		else:
			url += s[index]
		index += 1
	return url

print(urlify('Mr John Smith             ', 13))
