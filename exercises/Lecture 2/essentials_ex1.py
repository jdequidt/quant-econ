# Part 1
def innerproduct(x_vals,y_vals):
	"Calculates inner product of two vectors"
	if len(x_vals) != len(y_vals):
		return 'vectors have different lengths'
	else:
		innerproduct = 0
		for x,y in zip(x_vals,y_vals):
			innerproduct += x*y
		return innerproduct
	
print innerproduct([1,1,1],[2,2,2,2,2])
print innerproduct([1,1,1],[2,2,2])


# Part 2
print sum((j % 2) == 0 for j in range(100))

#Part 3

def countevenpairs(pairs):
	return sum((j[0] % 2 == j[1] % 2 == 0) for j in pairs)

pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
print countevenpairs(pairs)