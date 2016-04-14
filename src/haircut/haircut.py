#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np
from lib.search import binary_short

#Function that computes the number of people popped from the line at a given time
popped = lambda T,M : (1 + T//M).sum()

#Function that computes the barber number
def whichBarber(B,N,M):

	#Base case
	if N<=B:
		return N

	#Maximum amount of time so that N customers are popped from the line
	maxT = N*M.min()

	#Binary search for the time, safety check
	T_before = binary_short(0,maxT,N,popped,M=M)
	while True:
		if popped(T_before,M)>=N:
			T_before = T_before-1
		else:
			break

	assert popped(T_before,M)<N
	assert popped(T_before+1,M)>=N

	#Check which barbers get free at T+1
	popped_so_far = popped(T_before,M)
	free = list()
	
	for n,r in enumerate((T_before+1)%M):
		if r==0:
			free.append(n+1)

	#Compute the barber number
	return free[N-popped_so_far-1]


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read B,N,M
		B,N = [int(n) for n in line().split(" ")]
		M = np.array([int(n) for n in line().split(" ")])

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,whichBarber(B,N,M)))

if __name__=="__main__":
	main()