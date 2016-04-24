#!/usr/bin/env python
from __future__ import division
import sys

def minDenominations(C,D,V,denomination):

	#Can make change up to this value
	can_make_up_to = 0
	denominations_added = 0
	di = 0

	#Try to make up any value up to V; if not possible add denominations
	while can_make_up_to<V:

		if di<D and denomination[di]<=can_make_up_to+1:
			
			#No need to add denominations
			can_make_up_to+=C*denomination[di]
			di+=1
		
		else:

			#Need to add a new denomination
			new_denomination = can_make_up_to+1
			denominations_added+=1
			can_make_up_to += C*new_denomination

	#Return
	return denominations_added

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in C,D,V
		C,D,V = [ int(n) for n in line().split(" ") ]
		denomination = [ int(n) for n in line().split(" ") ]

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minDenominations(C,D,V,denomination)))

if __name__=="__main__":
	main()