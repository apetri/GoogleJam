#!/usr/bin/env python
from __future__ import division
import sys
import numpy as np

def minTime(pancakes,D):
	max_pancakes = pancakes.max()
	min_time = max_pancakes
	for t in range(max_pancakes-1,0,-1):
		proposed_time = (np.ceil(pancakes/t).astype(np.int) - 1).sum() + t
		if proposed_time<min_time:
			min_time = proposed_time

	return min_time

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in the number of diners D, the number of pancakes on each plate
		D = int(line())
		pancakes = np.array([ int(n) for n in line().split(" ") ])

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minTime(pancakes,D)))

if __name__=="__main__":
	main()