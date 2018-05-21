import math
import PIL

#It is vector compare: vector module and Hamming's distance between two vector-images
class Vector_Compare:
	def buildvector(im):
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
		return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

class Common_Vector_Compare(Vector_Compare):
	def compression(im, x, y):
		delta_x = im.size[0]//(x-1)
		delta_y = im.size[1]//(y-1)
		if delta_x == 1 and delta_y == 1:
			#The image does not need a compression
			return im
		im_new = Image.new("P", (x, y), 255)
		for i in range(x):
			for j in range(y):
				#Deviding into squares
				black, white = 0, 0
				for x_i in (i * delta_x, min((i + 1) * delta_x, size[0]), 1):
					for y_j in (i * delta_y, min((i + 1) * delta_y, size[1]), 1):
						pix = im.getpixel((x_i, y_j))
						if pix == 0:
							black = black + 1
						else:
							white = white + 1
				if black >= white:
					im_new.putpixel((i, j), 0)
		return im_new

	def creating_vectors(self, im1, im2):
		min_x = min(im1.size[0], im2.size[0])
		min_y = min(im1.size[1], im2.size[1])
		im1_new = Image.new("P", (min_x, min_y), 255)
		im2_new = Image.new("P", (min_x, min_y), 255)
		im1_new = self.compression(im1, min_x, min_y)
		im2_new = self.compression(im2, min_x, min_y)
		return (buildvector(im1), buildvector(im2))
