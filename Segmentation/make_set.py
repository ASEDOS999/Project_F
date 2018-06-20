import sys
sys.path.append("../Segmentation")

import PIL
from PIL import Image
import os
from segmentation import segmentation

def cut(path):
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
	border.string_border(im2)
	border.letter_border(im2)
	
	count = 100
	for letter in border.letters:
		if letter[0] - letter[2] < 0:
			im3 = im2.crop(letter)
			im3.save("./NEW_SETS/%s.gif"%(count))
		count = count + 1
	
	
