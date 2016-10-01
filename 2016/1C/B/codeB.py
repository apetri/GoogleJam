#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def configuration(B,M):
	
	if M>2**(B-2):
		return "IMPOSSIBLE"

	#Initialize array: build all slides with j>i (except from building 0)
	slides = np.zeros((B,B),dtype=np.int)
	i,j = np.indices(slides.shape)
	slides[j>i] = 1
	slides[0] = 0

	#Build the missing connections
	for b in range(B-2):
		if M&(2**b):
			slides[0,B-2-b] = 1

	if M==2**(B-2):
		slides[0,1:] = 1 

	#Return
	out = "POSSIBLE"
	for i in range(B):
		out += "\n"
		for j in range(B):
			out += str(slides[i,j])

	return out

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getstringlist = lambda : line().split(" ")
getint = lambda : int(line())
getintlist = lambda : [ int(n) for n in line().split(" ") ]


def main():

	#Number of test cases
	ntest = getint()

	#Cycle over test cases
	for t in range(ntest):
		
		#Input
		B,M = getintlist()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,configuration(B,M)))

if __name__=="__main__":
	main()