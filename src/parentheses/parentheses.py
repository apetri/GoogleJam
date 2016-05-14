#!/usr/bin/env python
from __future__ import division

import sys
import numpy as np

#DP table
def buildDPTable(N,K):

	#Initialize table: T(n,k) = number of possibilities in which digit n has offset k and all other digits before k have offset 0
	dp_table = np.zeros((N,)*2,dtype=np.int)
	dp_table[N-1] = 1

	#Always cycle over the last row of the table
	seen_so_far = 0
	for k in range(N):
		seen_so_far += dp_table[N-1,k]
		if seen_so_far>=K:
			return N-1,dp_table

	#Fill table top-down
	for n in range(N-2,-1,-1):
		
		dp_table[n,0] = dp_table[n+1].sum()
		seen_so_far = dp_table[n,0]

		for k in range(1,n+1):

			dp_table[n,k] = dp_table[n,k-1] - dp_table[n+1,k-1]
			seen_so_far += dp_table[n,k]

			#Doesn't make sense to fill the table anymore
			if seen_so_far>=K:
				return n,dp_table

	#K is too big
	return None

#Offsets
def buildParenthesesOffsets(N,K,dp_data):
	
	#Parentheses do not exist
	if dp_data is None:
		return None

	#Offsets
	offsets = np.zeros(N,dtype=np.int)

	#Get the data from the DP table
	n0,dp_table = dp_data
	start_k = 0

	#Walk down the digits
	for n in range(n0,N):

		current_sum = dp_table[n,start_k]
		previous_sum = 0

		for k in range(start_k,n+1):

			if current_sum>=K:

				offsets[n] = k
				start_k = k
				K-=previous_sum 

				break

			previous_sum = current_sum
			current_sum += dp_table[n,k+1]
			

	#Return the offsets
	return offsets


#Build parentheses
def buildParentheses(N,K,dp_data):

	offsets = buildParenthesesOffsets(N,K,dp_data)
	
	if offsets is None:
		return "Doesn't Exist!"

	parentheses = [")"]*2*N
	for n,off in enumerate(offsets):
		parentheses[n+off] = "("

	return "".join(parentheses)

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getintlist = lambda : [ int(c) for c in line().split(" ") ]

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read n,k
		N,K = getintlist()

		#Build DP table and calculate answer
		dp_data = buildDPTable(N,K)
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,buildParentheses(N,K,dp_data)))

if __name__=="__main__":
	main()