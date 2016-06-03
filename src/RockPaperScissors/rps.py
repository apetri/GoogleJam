#!/usr/bin/env python
from __future__ import division
import sys

#Wins over
wins_over = dict([("R","S"),("P","R"),("S","P")])

#Construct final lineup from the final winner
def construct_lineup(N,start,count):

	#Base case, there's only 1 player
	if N==0:
		return start

	#Must win again this candidate
	candidate = wins_over[start]
	count[candidate] += 1

	#Merge
	left = construct_lineup(N-1,start,count)
	right = construct_lineup(N-1,candidate,count)
	if left<right:
		return left + right
	else:
		return right + left



#Try the 3 possible lineups
def first_lineup(N,R,P,S):

	first = None

	for start in "RPS":

		#Keep track on the number of players
		count = dict([("R",0),("P",0),("S",0)])
		count[start] = 1 
		
		#Construct the proposed lineup and see if we can accept it
		proposed = construct_lineup(N,start,count)
		if (count["R"]!=R) or (count["P"]!=P) or (count["S"]!=S):
			continue
		
		if first is None:
			first = proposed
			continue

		if proposed<first:
			first = proposed

	if first is None:
		return "IMPOSSIBLE"

	return first


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
		
		N,R,P,S = getintlist()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,first_lineup(N,R,P,S)))

if __name__=="__main__":
	main()