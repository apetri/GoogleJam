from __future__ import division
import sys

#This routine is the one that solves the problem (recursive, guess what...)
def computeAB(n):

	if n==1:
		return 3,1
	elif n%2==0:
		a_half,b_half = computeAB(n//2)
		a_new = (a_half**2 + 5*(b_half**2))%1000
		b_new = (2*a_half*b_half)%1000
		return a_new,b_new
	else:
		a_half,b_half = computeAB(n//2)
		a_new = (3*(a_half**2) + 15*(b_half**2) + 10*a_half*b_half)%1000
		b_new = (a_half**2 + 5*(b_half**2) + 6*a_half*b_half)%1000
		return a_new,b_new


if __name__=="__main__":

	in_file = open(sys.argv[1],"r")
	out_file = open(sys.argv[1].replace(".in.",".out."),"w")

	#Read the number of test cases
	nTest = int(in_file.readline().strip("\n"))
	
	#Solve all the cases
	for n in range(nTest):

		num = int(in_file.readline().strip("\n"))
		an,bn = computeAB(num)
		out_file.write("Case #{0}: {1:03d}\n".format(n+1,(2*an-1)%1000))

	#Close files
	in_file.close()
	out_file.close()