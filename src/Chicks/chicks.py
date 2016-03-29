#!/usr/bin/env python

import sys
from functools import reduce
from operator import add

#Minimum number of swaps to get K of the N chickens to the distance B by time T
def minSwaps(x,v,K,B,T):

	#Total number of chickens
	N = len(x)

	#If K=0 we are good
	if K==0:
		return 0

	#Find out which chickens can make it
	can_make_it = list()
	cannot_make_it = list()

	for n in range(N):
		if (x[n] + v[n]*T) >= B:
			can_make_it.append(n)
		else:
			cannot_make_it.append(n)

	#If there are not enough of them return IMPOSSIBLE 
	if len(can_make_it)<K:
		return "IMPOSSIBLE"
	
	#Of all the ones that can make it, calculate the required number of swaps#
	required_swaps = list()
	for n in can_make_it:
		required_swaps.append(0)
		
		#A swap should occur only with a chicken that cannot make it
		for m in cannot_make_it:
			if m>n:
				required_swaps[-1] += 1

	#Pick K elements starting from the right of the required_swaps list and sum them 
	return reduce(add,required_swaps[-K:])

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read problem size, positions, velocities
		N,K,B,T = [ int(n) for n in line().split(" ") ]
		x = [ int(n) for n in line().split(" ") ]
		v = [ int(n) for n in line().split(" ") ]

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minSwaps(x,v,K,B,T)))

if __name__=="__main__":
	main()