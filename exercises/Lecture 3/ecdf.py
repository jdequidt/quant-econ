from __future__ import division
from random import uniform

class ecdf:
	def __init__(self, sample):
		self.observations = sample
	
	def __call__(self,x):
		return sum(i <= x for i in self.observations)/len(self.observations)

g = ecdf([1,2,3,4])
print g.observations
print g(3)


#testing
sample = [uniform(0, 1) for i in range(10)]
F = ecdf(sample)
print F(0.5)

F.observations = [uniform(0, 1) for i in range(1000)]
print F(0.5)