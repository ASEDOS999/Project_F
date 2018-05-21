import math
import PIL
import vector
import recog
import os
from segmentation import segmentation
from PIL import Image

new_elems = [] #set for new recognazable image

im = Image.open("TEST/1.gif")
#im = im.convert("P")
mas = im.histogram()
mas1 = im.histogram()
mas.sort()
mas.reverse()
first_max_color, sec_max_color = mas1.index(mas[0]), mas1.index(mas[1])

#CREATING NEW IMAGE


im2 = Image.new("P", im.size, 255)
temp = {}
for y in range(im.size[1]):
	for x in range(im.size[0]):
		pix = im.getpixel((x,y))
		temp[pix] = pix
		if pix != first_max_color: #what is more: letter or background?
			im2.putpixel((x,y),0)


#FILRATION
for x in range(im.size[0]):
	for y in range(im.size[1]):
		pix = im2.getpixel((x, y))
		if pix == 0:
			count = 0
			for i_x in range(-3, 3, 1):
				for i_y in range(-3, 3, 1):
					x_p = min(im2.size[0], max(0, x + i_x))
					y_p = min(im2.size[1], max(0, y + i_y))
					if im2.getpixel((x_p, y_p)) == 0:
						count += 1;
			if count < 2:
				im2.putpixel((x, y), 255)

im2.save("copy.png")

border = segmentation()
border.string_border(im2)
border.letter_border(im2)

#SIZE OF LABEL BETWEEN LETTERS AND BETWEEN WORDS

start, end, prev = 0, 0, 0
for letter in letters:
	if letter[1] == start and letter[3] == end:
		delta = letter[0] - prev
		if min > delta:
			min = delta
	start, end, prev = letter[1], letter[3], letter[2]

label = 3 * min #Let's think that labels are more than three times that spacing between letters

#CREATE VECTOR'S SET

set = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
set.extend(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))
set.extend(('?', ',', ':', ';')) #There isn't symbol of point
set.extend(('+', '-', '=', '<', '>'))
set.extend(new_elems) #if user decided to add new elems

imageset = []
for letter in set:
	for img in os.listdir('SET/%s'%(letter)):
		temp = []
		temp.append(vector.buildvector(Image.open('set/%s/%s'%(letter, img))))
		imageset.append((letter, temp))

#SIMPLE RECOGNITION OF SYMBOLS

v = vector.VectorCompare()
text_letter = []

for letter in letters:
	guess = []
	cutlet = im2.crop(letter)
	guess = recog.symb_recog(v, cutlet, imageset)
	guess.sort()
	text_letter.append(guess[0][1])
