import math

def calc(a, b, c):
	'''calculates all values of x for a given a b and c - answers are for qadratic equations in the following form: ax^2+bx+c=0'''
	x1=(-b+math.sqrt(b**2-4*a*c))/2*a
	x2=(-b-math.sqrt(b**2-4*a*c))/2*a
	return x1, x2
