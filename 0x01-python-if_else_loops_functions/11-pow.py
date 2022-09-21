#!/usr/bin/python3
def pow(a, b):
	if a == 0:
		return (0)
	if b == 0:
		return (1)
	elif a < 0:
		a = -a
		if b < 0:
			b = -b
			result = a ** b
			result = 1 / result
		else:
			result = a ** b
		result = -result
	elif a > 0:
		if b < 0:
			b = -b
			result = a ** b
			result = 1 / result
		else:
			result = a ** b
	return (result)
