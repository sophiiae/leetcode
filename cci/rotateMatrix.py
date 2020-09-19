# Given an image represented by an N x N matrix, where each pixel in the image is 4 byte. 
# Write a method to rotate the image by 90 degree. (in place)

def rotateMatrixOne (image):
	if (len(image) != len(image[0])):
		return
	n = len(image)
	for layer in range(0, n//2):
		first = layer
		last = n - 1 - layer
		for i in range(first, last):
			offset = i - first
			temp = image[first][i]
			image[first][i] = image[last-offset][first]
			image[last-offset][first] = image[last][last-offset]
			image[last][last-offset] = image[i][last]
			image[i][last] = temp
	return image

# logically this method works
def rotateMatrixTwo (image):
	if (len(image) != len(image[0])):
		return
	for i in range(0, len(image)):
		for j in range(0, len(image[0])):
			temp = image[i][j]
			image[i][j] = image[j][i]
			image[j][i] = temp
	# image is original image for this loop. doesn't get expected result
	for i in range(0, len(image)):
		for j in range(0, len(image[0])//2):
			temp = image[i][j]
			image[i][j] = image[i][len(image[0]) - 1 - j]
			image[i][len(image[0]) - 1 - j] = temp
	return image

matrix = [
	[1,2,3,4,5,6],
	[7,8,9,10,11,12],
	[13,14,15,16,17,18],
	[20,21,22,23,24,25],
	[31,32,33,34,35,36],
	[41,42,43,44,45,46]
]

print(rotateMatrixOne(matrix)) #rotated
print(rotateMatrixTwo(matrix)) #only fliped
