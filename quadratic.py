import math

def calc(a, b, c):
	x1=(-b+math.sqrt(b**2-4*ac))/2*a
	x2=(-b-math.sqrt(b**2-4*ac))/2*a
	return x1, x2
