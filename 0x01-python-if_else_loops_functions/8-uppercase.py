#!/usr/bin/python3
def uppercase(str):
	i = 0
	j = 0
	for x in str:
		j = j + 1
	for y in str:
		i = i + 1
		if y >= 'a' and y <= 'z':
			num = ord(y) - 32
			char = chr(num)
		else:
			char = y
		if i == j:
			print(char)
		else:
			print(char,end = '')
