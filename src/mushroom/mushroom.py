#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def minMushroom(sequence,N):

	minMushrooms1 = 0
	minMushrooms2 = 0
	minRate = 0
	
	for n in range(N-1):
		if sequence[n+1]<sequence[n]:
			diff = sequence[n]-sequence[n+1]
			minMushrooms1+=diff
			if diff>minRate:
				minRate = diff

	for n in range(N-1):
		if sequence[n]>minRate:
			minMushrooms2+=minRate
		else:
			minMushrooms2+=sequence[n]

	return minMushrooms1,minMushrooms2


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in N, sequence
		N = int(line())
		sequence = np.array([int(n) for n in line().split(" ")])

		#Calculate answer and output
		m1,m2 = minMushroom(sequence,N)
		sys.stdout.write("Case #{0}: {1} {2}\n".format(t+1,m1,m2))

if __name__=="__main__":
	main()