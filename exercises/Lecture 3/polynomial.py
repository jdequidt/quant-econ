class Polynomial:
	
	def __init__(self,coefficients):
		self.coefficients = coefficients
	
	def __call__(self,x):
		return sum(a*x**index for index, a in enumerate(self.coefficients))
		
	def differentiate(self):
		for i in range(len(self.coefficients)):
			self.coefficients[i] *= i
		self.coefficients.remove(0)
			
