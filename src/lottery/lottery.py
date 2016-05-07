#!/usr/bin/env python3

import sys
from functools import lru_cache

MAXBITS = 30

#Base case
base = {
	
	0 : 1,
	1 : 1,
	2 : 2,
	3 : 2,
	4 : 2,
	5 : 2,
	6 : 3,
	7 : 4
}

@lru_cache(maxsize=None)
def possibilities(A,B,K,maxbits=MAXBITS):
	
	#Base case
	bitA = A&2**(maxbits-1)
	bitB = B&2**(maxbits-1)
	bitK = K&2**(maxbits-1)

	if maxbits==1:
		return base[bitA*4+bitB*2+bitK]

	#Recursion
	remainderA = A%2**(maxbits-1) + 1
	remainderB = B%2**(maxbits-1) + 1

	#Separate the cases in which the leading K bit is 0 and 1
	base_possibilities = possibilities(A,B,K,maxbits-1)
	if bitK:

		if not(bitA) and not(bitB):
			return remainderA*remainderB
		elif bitA and not(bitB):
			return remainderB*(2**(maxbits-1)+remainderA)
		elif not(bitA) and bitB:
			return remainderA*(2**(maxbits-1)+remainderB)
		elif bitA and bitB:
			return base_possibilities + 2**(2*(maxbits-1)) + (2**(maxbits-1))*(remainderA+remainderB)

	else:
	
		#If the leading K bit is 0
		if not(bitA) and not(bitB):
			return base_possibilities
		elif not(bitA) and bitB:
			return base_possibilities + possibilities(A,bitB-1,K,maxbits-1)
		elif bitA and not(bitB):
			return base_possibilities + possibilities(bitA-1,B,K,maxbits-1)
		else:
			return possibilities(bitA-1,B,K,maxbits-1) + possibilities(A,bitB-1,K,maxbits-1) + possibilities(bitA-1,bitB-1,K,maxbits-1)

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
		
		A,B,K = getintlist()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,possibilities(A-1,B-1,K-1)))

if __name__=="__main__":
	main()