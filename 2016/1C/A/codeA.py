#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def evacuate(N,senators):

	nsen = 0
	total_senators = senators.sum()
	plan = list()

	while nsen<total_senators:

		to_evac = list()

		for n,s in enumerate(senators):
			
			if s>0:
				to_evac.append(chr(65+n))
				senators[n]-=1
				nsen+=1

		if len(to_evac)%2:
			last = to_evac.pop()
		else:
			last = None

		for p in range(len(to_evac)//2):
			plan.append(to_evac[2*p]+to_evac[2*p+1])

		if last is not None:
			plan.append(last)

	plan.reverse()
	return " ".join(plan)


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
		
		N = getint()
		senators = np.array(getintlist())

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,evacuate(N,senators)))

if __name__=="__main__":
	main()