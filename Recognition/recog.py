import math
import vector

#Argument: Object of class Common_Vector Compare(see vector.py); letter(image) that is being recognized; set of pair letter-Image_of_this_letter
def symb_recog(v, letter, set):
	guess = []
	for x in set:
		if letter[1] == -1 or letter[1] == x[2]:
			guess.append((v.new_relation(v.creating_vectors(x[1], letter[0])), x[0]))
	return guess
