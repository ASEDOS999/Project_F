from PIL import Image
import os

def symmetry(letter):
	x, y= letter.size
	vert, hor = 0.0, 0.0
	for i in range(x//2):
		for j in range(y):
			if letter.getpixel((i, j)) == letter.getpixel((x - i - 1, j)):
				vert = vert + 1
	vert = 2 * vert/ (x * y)
	if vert >= 0.8:
		vert = 1
	else:
		vert = 0
	for j in range(y//2):
		for i in range(x):
			if letter.getpixel((i, j)) == letter.getpixel((i, y - j - 1)):
				hor+=1
	hor = 2 * hor/(x * y)
	if hor >= 0.8:
		hor = 1
	else:
		hor = 0
	#(vert, hor)
	#class 0 - (0, 0)
	#class 1 - (1, 0)
	#class 2 - (0, 1)
	#class 3 - (1, 1)
	return (vert + 2 * hor)
