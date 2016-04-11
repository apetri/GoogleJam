#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

reverse = lambda s: s if len(s)<=1 else s[-1] + reverse(s[:-1])

def minCounts(N):

	#Base case 1
	if N<10:
		return N

	#Base case 2 
	if not(N%10):
		return 1 + minCounts(N-1)
	
	#String representation of N
	N_str = str(N)
	str_left = reverse(N_str[:len(N_str)//2])
	str_right = N_str[len(N_str)//2:]

	if int(str_left)>1:
		min_counts = int(str_left) + int(str_right)
	else: 
		min_counts = int(str_right)

	#Combine result
	return min_counts + minCounts(10**(int(np.log10(N))))


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read N
		N = int(line())

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minCounts(N)))

if __name__=="__main__":
	main()