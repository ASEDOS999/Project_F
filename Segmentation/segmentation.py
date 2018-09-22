#This module has class for segmentation into strings and letters
class segmentation():
	strings = []
	letters = []
	def string_border(self, im):
	        begin_string, end_string = 0, 0

	        #False = there aren't black pixels; True
		previous, str = False, False
		upd = 0

		for y in range(im.size[1]):
			previous = str
			str = False
			for x in range(im.size[0]):
				pix = im.getpixel((x,y))
				if pix != 255:
					#In this pixel's string there are black pixels
					str = True

				if str == True and previous == False:
					begin_string = y
					break


				if str == False and x == im.size[0] - 1:
					#In this pixel's string there aren't black pixels
					if previous == True:
						end_string = y - 1
						self.strings.append((begin_string, end_string))
		return 0

	def letter_border(self, im):
		inletter = False
		foundletter = False
		start_x = 0
		start_y = 0
		end_x = 0
		end_y = 0

		for string in self.strings:
			start = string[0]
			end = string[1]
			for x in range(im.size[0]):

				for y in range(start, end, 1):
					pix = im.getpixel((x,y))
					if pix == 0:
						inletter = True

				if foundletter == False and inletter == True:
					foundletter = True
					start_x = x

				#Finded letter has not more pixel in this column or this letter is not connected with current pixel
				if foundletter == True and (inletter == False):
					foundletter = False
					end_x = x
					black = False
					j = start
					while black == False:
						for i in range(start_x, end_x, 1):
							if im.getpixel((i, j)) == 0:
								black = True
						j+= 1
					f = end
					black = False
					while black == False:
						for i in range(start_x, end_x, 1):
							if im.getpixel((i, f)) == 0:
								black = True
						f-= 1
					self.letters.append((start_x, j-1, end_x, f+1))

				inletter=False
		return 0
