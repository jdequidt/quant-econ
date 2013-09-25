from random import uniform

def binomial_rv(n,p):
	y = 0
	for i in range(n):
		U = uniform(0,1)
		if U < p: y+=1
	return y