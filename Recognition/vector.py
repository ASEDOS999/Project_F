import math
import PIL
from PIL import Image
from fractions import gcd

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
		if len(concordance1) != len(concordance2):
			sys.exit()
		for i in range(len(concordance1)):
			if concordance1[i] == concordance2[i]:
				topvalue += 1
		return topvalue / len(concordance1)

	def new_relation(self, (im1, im2)):
		ret = 0.0
		if im1.size != im2.size:
			print "Non-equal sizes of images"
		for x in range(im1.size[0]):
			for y in range(im1.size[1]):
				if im1.getpixel((x, y)) == im2.getpixel((x, y)):
					ret += 1
		return ret /(im1.size[0]*im1.size[1])
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
		max_y = min(im1.size[1], im2.size[1])
		im1_new = Image.new("P", (max_x, max_y), 255)
		im2_new = Image.new("P", (max_x, max_y), 255)
		im1_new = self.grows(im1, max_x, max_y)
		im2_new = self.grows(im2, max_x, max_y)
		return ((im1_new), (im2_new))
