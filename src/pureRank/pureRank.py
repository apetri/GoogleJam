#!/usr/bin/env python

from __future__ import division

import sys
import numpy as np

from lib.binomial import Binomial

class CombCalculator(Binomial):

	def __init__(self,maxN=501,modulo=100003):
		
		super(CombCalculator,self).__init__(maxN,modulo)
		
		#Initialize with boundary conditions
		self._combinations = np.ones_like(self._binomial) * -1
		n,k = np.indices(self._combinations.shape)
		self._combinations[k>=n] = 0
		self._combinations[n<2] = 0
		self._combinations[k==0] = 0
		self._combinations[k==1] = 1
		self._combinations[k==2] = 1


	#Compute combinations where n has rank k
	def combinations(self,n,k):
		if self._combinations[n,k]>-1:
			return self._combinations[n,k]

		for ni in range(2,n+1):
			for ki in range(2,k+1):
				result = 0
				for li in range(1,k):
					result = (result + (self._combinations[ki,li]*self.binomial(ni-ki-1,ki-li-1))%self._modulo)%self._modulo
				self._combinations[ni,ki] = result

		return result

	#How many different subsets of (2..n) are pure with respect to n
	def numPure(self,n):
		result = 0
		for k in range(1,n):
			result = (result + self.combinations(n,k))%self._modulo

		return result 

		

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Fill in tables
	calculator = CombCalculator(51)
	calculator.binomial(50,49)
	calculator.combinations(50,49)

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):

		#Read in n
		n = int(line())

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,calculator.numPure(n)))

if __name__=="__main__":
	main()