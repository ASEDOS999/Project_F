import math
import PIL
from PIL import Image

#It is vector compare: vector module and Hamming's distance between two vector-images
class Vector_Compare:
	def buildvector(self, im):
		d1 = {}
		count = 0
		for i in im.getdata():
			d1[count] = i
			count += 1
		return d1

	def magnitude(self,concordance):
		total = 0
		for word,count in concordance.iteritems():
			total += count ** 2
		return math.sqrt(total)

	def relation(self, (concordance1, concordance2)):
		#Euclid's scalar product
		relevance = 0
		topvalue = 0
		for word, count in concordance1.iteritems():
			if concordance2.has_key(word):
				topvalue += count * concordance2[word]
		return topvalue / max(1, (self.magnitude(concordance1) * self.magnitude(concordance2)))

class Common_Vector_Compare(Vector_Compare):
	def compression(self, im, x, y):
		pix = 0
		delta_x = max(im.size[0]//(x-1), 0)
		delta_y = max(im.size[1]//(y-1), 0)
		if delta_x == 1 and delta_y == 1:
			#The image does not need a compression
			return im
		im_new = Image.new("P", (x, y), 255)
		for i in range(x):
			for j in range(y):
				#Deviding into squares
				black, white = 0, 0
				for x_i in (min(i * delta_x, im.size[0] - 1), min((i + 1) * delta_x, im.size[0] - 1), 1):
					for y_j in (min(j * delta_y, im.size[1] - 1), min((j + 1) * delta_y, im.size[1] - 1), 1):
						pix = im.getpixel((x_i, y_j))
						if pix == 0:
							black = black + 1
						else:
							white = white + 1
				if black >= white:
					im_new.putpixel((i, j), 0)
		return im_new

	#help function for image's homomorphism
	def f(self, x, zoom, rem):
		if (x // (zoom + 1) < rem):
			return (x // (zoom+1))
		else:
			return ((x - rem) // zoom)

	#new function for zoom
	def grows(self, im, x, y):
		im_new = Image.new("P", (x, y), 255)
		zoom_x, zoom_y = x // im.size[0], y // im.size[1]
		rem_x, rem_y = x % im.size[0], y % im.size[1]
		for i in range(x):
			for j in range(y):
				a = im.getpixel((self.f(i, zoom_x, rem_x), self.f(j, zoom_y, rem_y)))
				if a == 0:
					im_new.putpixel((i, j), 0)
		return im_new

	def creating_vectors(self, im1, im2):
		max_x = max(im1.size[0], im2.size[0])
		max_y = max(im1.size[1], im2.size[1])
		im1_new = Image.new("P", (max_x, max_y), 255)
		im2_new = Image.new("P", (max_x, max_y), 255)
		im1_new = self.grows(im1, max_x, max_y)
		im2_new = self.grows(im2, max_x, max_y)
		return (self.buildvector(im1_new), self.buildvector(im2_new))
