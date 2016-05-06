#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def minMoves(strings):

	#Number of strings
	N = len(strings)
	characters = list()
	character_count_first = list()

	#Use the first string as template
	s0 = strings[0]
	current_char = s0[0]
	characters.append(current_char)
	character_count_first.append(1)

	for c in s0[1:]:

		if c==current_char:
			character_count_first[-1]+=1
		else:
			characters.append(c)
			current_char = c
			character_count_first.append(1)

	#Proceed with the other strings
	character_count = np.zeros((N,len(characters)),dtype=np.int)
	character_count[0] = character_count_first

	for ns,string in enumerate(strings[1:]):
		
		current_point = 0
		compare_to = characters[current_point]
		current_char = string[0]

		if current_char!=compare_to:
			return "Fegla Won"

		character_count[ns+1,current_point] = 1

		for c in string[1:]:
			
			if c!=current_char:

				current_point+=1

				if current_point>=len(characters):
					return "Fegla Won"

				compare_to = characters[current_point]
				
				if c!=compare_to:
					return "Fegla Won"

				current_char=c
				character_count[ns+1,current_point]+=1

			else:
				character_count[ns+1,current_point]+=1

		if current_point!=(len(characters)-1):
			return "Fegla Won"

	#Compute the minimum number of moves
	moves = 0
	for nc in range(len(characters)):
		count = character_count[:,nc]
		current_min = np.abs(count-count[0]).sum()
		
		for med in range(count.min(),count.max()+1):
			proposed_min = np.abs(count-med).sum()
			if proposed_min<current_min:
				current_min = proposed_min

		moves += current_min

	return moves


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
		
		#Get the strings
		N = getint()
		strings = list()
		for n in range(N):
			strings.append(line())

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minMoves(strings)))

if __name__=="__main__":
	main()