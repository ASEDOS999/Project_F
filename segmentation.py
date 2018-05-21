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
		last_column, current_column = [], []

		for string in self.strings:
			start = string[0]
			end = string[1]
			for x in range(im.size[0]):
				last_column = current_column
				current_column = []
				sum = 0
				k = 1

				for y in range(start, end, 1):
					pix = im.getpixel((x,y))
					current_column.append(pix)
					if pix == 0:
						inletter = True
				"""
				#Connectivity_check
				if x == 0:
					k = 1
				else:
					for i in range(len(current_column)):
						if last_column[i] != 255 and current_column[i] != 255:
							sum += 1
					if sum > 0:
						k = 1
				"""
				if foundletter == False and inletter == True:
					foundletter = True
					start_x = x

				#Finded letter has not more pixel in this column or this letter is not connected with current pixel
				if foundletter == True and (inletter == False or k == 0):
					foundletter = False
					end_x = x
					self.letters.append((start_x, start, end_x, end))

				inletter=False
		return 0
