import math
import vector

def symb_recog(v, letter, set): #object of class Vector Compare, letter(im.crop) that is being recognized and set that is used for recognition
	guess = []
	for image in set:
		for x,y in image.iteritems():
			if len(y) != 0:
				guess.append((v.relation(v.creating_vectors(y[0], im)), x))
	return guess
