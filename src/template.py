#!/usr/bin/env python

import sys

#Methods for solving problem#

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Solve the problem#

		#Calculate answer and output
		sys.stdout.write("Case #{0}: \n".format(t+1))

if __name__=="__main__":
	main()