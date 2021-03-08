import re
def mostCommonWord(paragraph: str, banned) -> str:
	paragraph = re.sub(r'[^\w\s]', ' ', paragraph)  # remove special characters
	paragraph = paragraph.lower()

	words = paragraph.split()
	table = {}

	for word in words:
		if word not in banned:
			table[word] = table.get(word, 0) + 1
			
	most = None
	count = 0
	for word in table.keys():
		if table[word] > count:
			most = word
			count = table[word]
	return most

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

p2 = "a."
banned2 = []

print(mostCommonWord(paragraph, banned))
print(mostCommonWord(p2, banned2))
