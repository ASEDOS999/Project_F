import math
import PIL
import vector
from PIL import Image

im = Image.open("TEST/1.png")
im = im.convert("P")
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

im2 = Image.new("P", im.size, 255)

#FILRATION
for x in range(im.size[0]):
	for y in range(im.size[1]):
		pix = im2.getpixel((x, y))
		if pix == 0:
			count = 0
			for i_x in range(-3, 3, 1):
				for i_y in range(-3, 3, 1):
					x_p = min(im.size[0], max(0, x + i_x))
					y_p = min(im.size[1], max(0, y + i_y))
					if im2.getpixel((x_p, y_p)) == 0:
						count += 1;
			if count < 2:
				im2.putpixel((x, y), 255)
			else:
				im2.putpixel((x, y), 0)


#STRING'S BORDER
strings = []
begin_string, end_string = 0, 0

#False = there aren't black pixels; True
previous, str = False, False
upd = 0

for y in range(im2.size[1]):
	previous = str
	str = False
	for x in range(im2.size[0]):
		pix = im2.getpixel((x,y))
		if pix == 0:
			#In this pixel's string there are black pixels
			str = True

		if str == True:
			if previous == False:
				begin_string = y
			break


		if str == False and x == im2.size[0]:
			#In this pixel's string there aren't black pixels
			if previous == True:
				end_string = y - 1
				strings.append((begin_string, end_string))
#LETTER'S BORDER
inletter = False
foundletter = False
start_x = 0
start_y = 0
end_x = 0
end_y = 0

letters = []

for string in strings:
	start = string[0]
	end = string[0]
	for x in range(im2.size[0]):
		for y in range(start, end, 1):
			pix = im2.getpixel((x,y))
			if pix == 0:
				inletter = True

			if foundletter == False and inletter == True:
				foundletter = True
				start_x = x

			if foundletter == True and inletter == False:
				foundletter = False
				end_x = x
				letters.append((start_x, end_x))

			inletter=False
print (letters)

#SIZE OF LABEL BETWEEN LETTERS AND BETWEEN WORDS

