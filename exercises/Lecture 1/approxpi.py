from __future__ import division
from random import uniform
from math import sqrt

n = 10000000

count = 0
for i in range(n):
	u,v = uniform(0,1),uniform(0,1)
	d = sqrt(u**2 + v**2)
	if d < 1: count += 1

print 4*(count/n)