# check if s2 is a rotation of s1.
# i.e. "waterbottle" is a rotation of "erbottlewat"

def stringRotate(s1: str, s2: str):
	if (len(s1) != len(s2)):
		return False
	j, rotatePoint = 0, 0
	for i in range(0, len(s1)):
		if (s1[i] == s2[j]):
			j += 1
		else:
			j = rotatePoint
			if (s1[i] == s2[j]):
				j += 1
	rotatePoint = j
	i = 0
	while (rotatePoint < len(s2)):
		if (s1[i] != s2[rotatePoint]):
			return False
		i += 1
		rotatePoint += 1
	return True

print(stringRotate('waterbottle', 'bottlewater')) #true
print(stringRotate('helloworld', 'dhelloworl')) #true
print(stringRotate('helloworld', 'helleworld')) #false
print(stringRotate('helloworld', 'dheeloworl')) #false
print(stringRotate('aaaaa', 'aabaa')) #false
