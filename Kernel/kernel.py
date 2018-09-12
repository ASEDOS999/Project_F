import sys
sys.path.append("./Segmentation")
sys.path.append("./Recognition")
sys.path.append("./Interface")

import math
import PIL
import vector
import recog
import os
from segmentation import segmentation
from PIL import Image


def text(set, path):
	im = Image.open("../../../%s"%(path))
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


	border = segmentation()
	border.strings, border.letters = [], []
	border.string_border(im2)
	border.letter_border(im2)

	strings, letters = border.strings, border.letters
	#SIZE OF LABEL BETWEEN LETTERS AND BETWEEN WORDS

	delta = 0
	for letter in letters:
		delta = delta + (letter[2] - letter[0])
	delta = delta / len(letters)


	label = 0.5 * delta #Let's think that label has size that is close to letter's size

	set_label = []
	place_label = 0
	start, end, prev = 0, 0, 0
	for letter in letters:
		if letter[1] == start and letter[3] == end:
			delta = letter[0] - prev
			if delta >= label:
				set_label.append((place_label, ' '))
			else:
				set_label.append((place_label, ''))
		else:
			if start != 0 or end != 0:
				set_label.append((place_label, '\n'))
			else:
				set_label.append((place_label, ''))
		place_label += 1
		start, end, prev = letter[1], letter[3], letter[2]

	#SIMPLE RECOGNITION OF SYMBOLS

	imageset = []
	for i in set:
		for img in os.listdir('%s'%(i[1])):
			temp = Image.open('%s/%s'%(i[1], img))
			imageset.append((i[0], temp))

	v = vector.Common_Vector_Compare()
	text_letter = []
	z = 100
	for letter in letters:
		v.count = z
		guess = []
		cutlet = im2.crop(letter)
		guess = recog.symb_recog(v, cutlet, imageset)
		guess.sort()
		text_letter.append(guess[len(guess) - 1][1])
		z = z + 100
	output = open('out.txt', 'w')

	number_letter = 0
	k = set_label.pop(0)
	for i in text_letter:
		if number_letter == k[0]:
			output.write(k[1])
			if len(set_label) > 0:
				k = set_label.pop(0)
		output.write(i)
		number_letter += 1
	text_letter = []
	output.close()

