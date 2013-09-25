def factorial(x):
	if not ((x % 1 == 0) & (x > 0)):
		return "not a positive integer"
	else:
		factorial = 1
		while x > 1:
			factorial *= x
			x -= 1
		return factorial