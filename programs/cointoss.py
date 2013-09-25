from random import uniform
import sys

win = 0
headcount = 0
for i in range(10):
	headcount = headcount + 1 if (uniform(0,1) < 0.5) else 0
	if headcount == 3:
		win = 1

if win == 1:
	print "you win"
else:
	print "you lose"