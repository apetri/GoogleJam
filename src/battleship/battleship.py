#!/usr/bin/env python
from __future__ import division
import sys

def guarantee(R,C,W):

	if R==1:
		return W + (C-1)//W
	else:
		return (R-1)*(C//W) + W + (C-1)//W 

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read input 
		R,C,W = [int(n) for n in line().split(" ")]

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,guarantee(R,C,W)))

if __name__=="__main__":
	main()