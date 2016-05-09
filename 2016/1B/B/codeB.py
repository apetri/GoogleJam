#!/usr/bin/env python
from __future__ import division
import sys

def replace_best(pd,pc,pj,bd,bc,bj):

	if pd<bd:
		return pd,pc,pj

	if pd==bd:
		
		if pc<bc:
			bc = pc

		if pj<bj:
			bj = pj

		return bd,bc,bj

	return bd,bc,bj


def optimize(c,j):

	N = len(c)
	
	best_c = c.replace("?","9")
	best_j = j.replace("?","0")
	best_diff = abs(int(best_c)-int(best_j))
	common_prefix = ""

	#Cycle over letters
	for n in range(N):

		#If the digits are the same (and not question marks)
		if c[n]==j[n] and c[n].isdigit():
			common_prefix+=c[n]

		elif c[n]==j[n] and c[n]=="?":

			for (dc,dj) in ((0,1),(1,0)):
				
				proposed_c = str(dc) + c[n+1:].replace("?",str((9+dc)%10))
				proposed_j = str(dj) + j[n+1:].replace("?",str((9+dj)%10))
				proposed_diff = abs(int(proposed_c)-int(proposed_j))

				proposed_c = common_prefix + proposed_c
				proposed_j = common_prefix + proposed_j
				best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j)

			common_prefix += "0"

		elif c[n]=="?":

			if j[n]>"0":

				proposed_c = str(int(j[n])-1) + c[n+1:].replace("?","9")
				proposed_j = j[n:].replace("?","0") 
				proposed_diff = abs(int(proposed_c)-int(proposed_j))

				proposed_c = common_prefix + proposed_c
				proposed_j = common_prefix + proposed_j
				best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j) 

			if j[n]<"9":
				
				proposed_c = str(int(j[n])+1) + c[n+1:].replace("?","0")
				proposed_j = j[n:].replace("?","9") 
				proposed_diff = abs(int(proposed_c)-int(proposed_j)) 

				proposed_c = common_prefix + proposed_c
				proposed_j = common_prefix + proposed_j
				best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j)

			common_prefix += j[n]

		elif j[n]=="?":

			if c[n]<"9":
				
				proposed_j = str(int(c[n])+1) + j[n+1:].replace("?","0")
				proposed_c = c[n:].replace("?","9") 
				proposed_diff = abs(int(proposed_c)-int(proposed_j))

				proposed_c = common_prefix + proposed_c
				proposed_j = common_prefix + proposed_j
				best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j) 

			if c[n]>"0":

				proposed_j = str(int(c[n])-1) + j[n+1:].replace("?","9")
				proposed_c = c[n:].replace("?","0") 
				proposed_diff = abs(int(proposed_c)-int(proposed_j)) 

				proposed_c = common_prefix + proposed_c
				proposed_j = common_prefix + proposed_j
				best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j)

			common_prefix += c[n]

		elif c[n]>j[n]:
			
			proposed_c = c[n:].replace("?","0")
			proposed_j = j[n:].replace("?","9")
			proposed_diff = abs(int(proposed_c)-int(proposed_j)) 

			proposed_c = common_prefix + proposed_c
			proposed_j = common_prefix + proposed_j
			best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j)

			break

		elif c[n]<j[n]:

			proposed_c = c[n:].replace("?","9")
			proposed_j = j[n:].replace("?","0")
			proposed_diff = abs(int(proposed_c)-int(proposed_j)) 

			proposed_c = common_prefix + proposed_c
			proposed_j = common_prefix + proposed_j
			best_diff,best_c,best_j = replace_best(proposed_diff,proposed_c,proposed_j,best_diff,best_c,best_j)

			break

	if len(common_prefix)==N:
		return common_prefix,common_prefix

	return best_c,best_j


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
		
		c,j = getstringlist()

		#Calculate answer and output
		newc,newj = optimize(c,j)
		sys.stdout.write("Case #{0}: {1} {2}\n".format(t+1,newc,newj))

if __name__=="__main__":
	main()