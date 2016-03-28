from __future__ import division

import sys
import numpy as np

modulo = 1000000007

def possibleCombinations(n,k):

	#Dynamic programming table
	table = np.zeros((n+1,k+1),dtype=np.int)

	#Base recursion case
	table[0,0] = 1

	#Solve the recursion using dynamic programming in O(nk) time
	for i in range(1,n+1):
		for j in range(1,min(i,k)+1):
			table[i,j] = (j * (table[i-1,j] + table[i-1,j-1])) % modulo

	#Return the answer
	return table[n,k]


#Main execution
if __name__=="__main__":

	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")

	output = file(output_filename,"w")

	#Process input case by case
	with open(input_filename,"r") as infile:

		#Number of test cases
		nTest = int(infile.readline().rstrip("\n"))

		#Solve each test case
		for t in range(nTest):

			#Read n and k
			k,n = [ int(l) for l in infile.readline().rstrip("\n").split(" ") ]

			#Write the answer
			output.write("Case #{0}: {1}\n".format(t+1,possibleCombinations(n,k)))

	#Close output
	output.close()