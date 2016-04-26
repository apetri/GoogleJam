#!/usr/bin/env python
from __future__ import division
import sys

#Compute the maximum overlap between a string and its suffixes O(N^2)
def maxOverlap(s):
	overlap = 0
	for n in range(1,len(s)):
		if s[-n:]==s[:n] and n>overlap:
			overlap = n

	return overlap

#Compute the probability of typing the target word
def probTarget(target,keyboard):

	#Keep track of the number of times a character appears
	count = dict()
	for k in keyboard:
		if k in count:
			count[k]+=1
		else:
			count[k] = 1

	#Compute the probability
	prob = 1.
	for t in target:
		if t not in count:
			return 0.
		prob*=count[t]/len(keyboard)

	#Return
	return prob

#Solve the problem
def expBananas(K,L,S,target,keyboard):

	#Compute the probability of typing the word
	prob = probTarget(target,keyboard)
	if prob==0.:
		return 0.

	#Compute the maximum overlap of the target word, and the maximum number of bananas
	overlap = maxOverlap(target)
	maxBananas = 1 + (S-L)//(L-overlap)

	#Compute the expected number of bananas to keep
	expToGive = prob*(1+S-L)
	return maxBananas-expToGive

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")
getstring = lambda : line()
getint = lambda : int(line())
getintlist = lambda : [ int(n) for n in line().split(" ") ]


def main():

	#Number of test cases
	ntest = getint()

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in input
		K,L,S = getintlist()
		keyboard = getstring()
		target = getstring()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1:.7f}\n".format(t+1,expBananas(K,L,S,target,keyboard)))

if __name__=="__main__":
	main()