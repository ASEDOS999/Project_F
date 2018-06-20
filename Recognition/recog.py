import math
import vector

#Argument: Object of class Common_Vector Compare(see vector.py); letter(image) that is being recognized; set of pair letter-Image_of_this_letter
def symb_recog(v, letter, set):
	guess = []
	for x in set:
		guess.append((v.relation(v.creating_vectors(x[1], letter)), x[0]))
	return guess
