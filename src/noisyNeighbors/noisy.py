#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np

def minNoise(R,C,N):

	#Obvious
	if N==0:
		return 0

	if R*C==1:
		return 0
	
	#Distinguish cases in which the number of cells is even or odd
	if R*C%2:

		X = max(R,C)
		Y = min(R,C)

		if Y==1:
			noise = np.empty(R*C,dtype=np.int)
			noise[:X//2+1] = 0
			noise[X//2+1:] = 2
			assert noise.sum()==C*(R-1)+R*(C-1),"{0} {1}".format(R,C)
			return noise.cumsum()[N-1]

		#If X>1,Y>1, X and Y are odd we need to consider two chessboard cases
		noise1 = np.empty(R*C,dtype=np.int)
		noise2 = np.empty(R*C,dtype=np.int)

		#First chessboard
		chessboard = (X//2) * (Y//2+1) + (Y//2) * (X//2+1)
		noise1[:chessboard] = 0

		corners = 4
		noise1[chessboard:chessboard+corners] = 2

		boundary = 2*((Y-2)//2+(X-2)//2)
		noise1[chessboard+corners:chessboard+corners+boundary] = 3
		noise1[chessboard+corners+boundary:] = 4


		#Second chessboard
		chessboard = (X//2+1)*(Y//2+1) + (X//2)*(Y//2)
		noise2[:chessboard] = 0

		#No corners, compute the boundaries
		boundaries = 2*(X//2 + Y//2)
		noise2[chessboard:chessboard+boundaries] = 3
		noise2[chessboard+boundaries:] = 4

		assert noise1.sum()==C*(R-1)+R*(C-1),"{0} {1}".format(R,C)
		assert noise2.sum()==C*(R-1)+R*(C-1),"{0} {1}".format(R,C)
		return min(noise1.cumsum()[N-1],noise2.cumsum()[N-1])

	else:

		#Lookup table
		noise = np.empty(R*C,dtype=np.int)

		#Find the even dimension
		if R%2:
			X=C
			Y=R
		else:
			X=R
			Y=C

		#Fill in chessboard
		chessboard = Y*(X//2)
		noise[:chessboard] = 0

		if Y==1:
			corners = 1
			noise[chessboard:chessboard+corners] = 1
			noise[chessboard+corners:] = 2
		else:

			#Fill in corners
			corners = 2
			noise[chessboard:chessboard+corners] = 2

			#Boundary cells
			boundary = (X//2 - 1)*2 + Y-2
			noise[chessboard+corners:chessboard+corners+boundary] = 3

			#Rest
			noise[chessboard+corners+boundary:] = 4

		assert noise.sum()==C*(R-1)+R*(C-1),"{0} {1}".format(R,C)
		return noise.cumsum()[N-1]

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):
		
		#Read in R,C,N
		R,C,N = [ int(n) for n in line().split(" ") ]

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minNoise(R,C,N)))

if __name__=="__main__":
	main()