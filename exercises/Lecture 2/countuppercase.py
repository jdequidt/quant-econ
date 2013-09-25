def countuppercase(string):
	return sum(x.upper() == x for x in string)
	
print countuppercase('HIHIHI')
print countuppercase('hihihi')
print countuppercase('HiHiHi')