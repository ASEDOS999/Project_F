#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("./Interface")
sys.path.append("./Segmentation")
sys.path.append("./Kernel")
import interface

i = 0
inp = open('Recognition/list_of_set.txt')
line = inp.readline()
current_set = []
v = interface.window()
while line:
	if line == '}\n':
		i = 0
		v.set_of_set.append((name, current_set))
		current_set = []
	if i == 1:
		current_set.append((line[0],line[2:len(line)-3], int(line[len(line) - 2:len(line) - 1])))
	if line == '{\n':
		i = 1
	if i == 0 and line != '}\n':
		name = line[0:len(line) - 1]

	line = inp.readline()

inp.close()
v.color_bg, v.color_text, v.style_text = 'grey', 'black', 'arial 14 bold'
v.start()

