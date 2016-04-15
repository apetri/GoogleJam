#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def minCuts(N,x,y):

	if N<=3:
		return [0]*N

	min_cuts = list()
	for n in range(N):
		x0 = x[n]
		y0 = y[n]
		
		#Partition the plane and count the number of points on either side
		partition = (x[:,None]-x0)*(y[None]-y0) - (y[:,None]-y0)*(x[None]-x0)
		optimal_partition = np.minimum((partition>0).sum(-1),(partition<0).sum(-1))
		optimal_partition[n] = N

		min_cuts.append(optimal_partition.min())

	return min_cuts


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read input (N,x,y)
		N = int(line())
		x = np.empty(N,dtype=np.int)
		y = np.empty(N,dtype=np.int)
		for n in range(N):
			x[n],y[n] = [ int(c) for c in line().split(" ") ]

		#Calculate answer and output
		sys.stdout.write("Case #{0}: \n".format(t+1))
		for c in minCuts(N,x,y):
			sys.stdout.write("{0}\n".format(c))

if __name__=="__main__":
	main()