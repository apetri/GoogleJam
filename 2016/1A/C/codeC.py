#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

#Vertex types
UNDECIDED = 0
JOIN = 1
CYCLE = 2
CHAIN = 3
NONVIABLE = 4

def maxCircle(N,bff):

	#Vertex types
	vertex_type = np.zeros_like(bff)

	#Maximum cycle and chain length
	max_cycle = 0
	longest_chain = np.ones_like(bff)*-1

	#Cycle over vertices to decide which ones are joins
	for n in range(1,N+1):
		if bff[bff[n-1]-1]==n:
			vertex_type[n-1] = JOIN
			longest_chain[n-1] = 1

	#Cycle over vertices to decide which ones are cycles, chains, non-viable
	for n in range(1,N+1):
		visited_in_path = set()

		#Proceed only if undecided
		if vertex_type[n-1]==UNDECIDED:
			current = n
			visited_in_path.add(n)

			#Walk the path from this vertex
			while True:

				current = bff[current-1]

				#If we already walked across this vertex we found a cycle
				if current in visited_in_path:
					
					vertex_type[current-1] = CYCLE

					#We need to find the length of the cycle
					cycle_length = 1
					cycle_start = current
					visited_in_path.discard(current)
					next_in_cycle = bff[cycle_start-1]
					while next_in_cycle!=cycle_start:
						cycle_length+=1
						visited_in_path.discard(next_in_cycle)
						vertex_type[next_in_cycle-1] = CYCLE
						next_in_cycle = bff[next_in_cycle-1]

					#Update the max length of the cycle
					if cycle_length>max_cycle:
						max_cycle = cycle_length

					#Mark the other vertices on the path as nonviable
					for v in visited_in_path:
						vertex_type[v-1] = NONVIABLE

					#Finally break
					break

				visited_in_path.add(current)

				if vertex_type[current-1]==JOIN:
					visited_in_path.discard(current)
					for v in visited_in_path:
						vertex_type[v-1] = CHAIN
					break

				if vertex_type[current-1]==CHAIN:
					visited_in_path.discard(current)
					for v in visited_in_path:
						vertex_type[v-1] = CHAIN
					break

				if vertex_type[current-1] in [CYCLE,NONVIABLE]:
					visited_in_path.discard(current)
					for v in visited_in_path:
						vertex_type[v-1] = NONVIABLE
					break


	#Now we decided what each vertex is, we can decide the maximum chain lengths
	#TODO: Naive approach, for each CHAIN vertex, walk until the join
	for n in range(1,N+1):
		
		if vertex_type[n-1]!=CHAIN:
			continue

		#We are on a chain vertex, walk until the join
		current = n
		chain_length = 1
		while vertex_type[current-1]!=JOIN:
			current = bff[current-1]
			chain_length+=1

		#Update the maximum chain length
		if longest_chain[current-1]<chain_length:
			longest_chain[current-1]=chain_length

	#Now we can decide the maximum circle size 
	return max(max_cycle,longest_chain[longest_chain>0].sum())


#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in N,bff
		N = int(line())
		bff = np.array([int(n) for n in line().split(" ")])

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,maxCircle(N,bff)))

if __name__=="__main__":
	main()