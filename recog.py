import math
import PIL #work with images
from PIL import Image

im = Image.open("image2.png")
im = im.convert("P")
mas = im.histogram()
mas1 = im.histogram()
mas.sort()
mas.reverse()
first_max_color, sec_max_color = mas1.index(mas[0]), mas1.index(mas[1])

#CREATING NEW IMAGE
im2 = Image.new("P", im.size, 255)
temp = {}
for x in range(im.size[1]):
	for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		temp[pix] = pix
		if pix == sec_max_color: #what is more: letter or background?
			im2.putpixel((y,x),0)

print (im2.histogram())
im2.save("copy.png")
"""
#Letter's Border
inletter = False
foundletter=False
start = 0
end = 0

letters = []

for y in range(im2.size[0]): # slice across
	for x in range(im2.size[1]): # slice down
		pix = im2.getpixel((y,x))
		if pix != 255:
			inletter = True
		if foundletter == False and inletter == True:
			foundletter = True
			start = y

		if foundletter == True and inletter == False:
			foundletter = False
			end = y
			letters.append((start,end))

		inletter=False
print (letters)

"""
