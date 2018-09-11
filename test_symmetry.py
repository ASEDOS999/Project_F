from PIL import Image
import os

def symmetry(letter):
	x, y= letter.size
	vert, hor = 0.0, 0.0
	for i in range(x//2):
		for j in range(y):
			if letter.getpixel((i, j)) != letter.getpixel((x - i - 1, j)):
				vert = vert + 1
	vert = vert/ (x * y)

	for j in range(y//2):
		for i in range(x):
			if letter.getpixel((i, j)) == letter.getpixel((i, y - j - 1)):
				hor+=1
	hor = hor / (x * y)
	return (vert, hor)

set = ['0','1','2','3','4','5','6','7','8','9','0']
set = set + ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
set = set + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
set = set + ['+', '-', '=', '<', '>']
set = set + ['?', ',', ':', ';', '!']



for i in set:
	for j in os.listdir("SET/%s"%(i)):
		let = Image.open("SET/%s/%s"%(i, j))
		print i, symmetry(let)


