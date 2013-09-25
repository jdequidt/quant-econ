def p(x,coeff):
	return sum(a*x**index for index, a in enumerate(coeff))
    
print p(2,[1,2,5,8])
		