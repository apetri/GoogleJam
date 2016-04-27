#!/usr/bin/env python
from __future__ import division
import sys

#Methods for solving problem#

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
		
		#Solve the problem#

		#Calculate answer and output
		sys.stdout.write("Case #{0}: \n".format(t+1))

if __name__=="__main__":
	main()