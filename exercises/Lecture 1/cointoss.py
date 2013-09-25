from random import uniform
import sys
import numpy

def gamble(tosses,headsequence):
	headcount = 0
	for i in range(tosses):
		headcount = headcount + 1 if (uniform(0,1) < 0.5) else 0
		if headcount == headsequence:
			return 'after ' + str(i) + ' tries, you win'
	return 'you lose'

print gamble(10000000,20)

