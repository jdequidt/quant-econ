#!/Users/Jon/anaconda/bin/python

from pylab import plot, show, legend
from random import normalvariate

T = 200
alphavector = [0,0.8,0.98]

for alpha in alphavector:
	x = [0]
	for j in range(T):
		x.append(alpha * x[j] + normalvariate(0,1))
	plot(x, label = 'alpha = ' + str(alpha))

legend()	
show()