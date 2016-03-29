import sys
import numpy as np


def minscalar(x,y):
	x_s = np.sort(x)
	y_s = -np.sort(-y)
	return np.dot(x_s,y_s)

#Read in input file
in_file = open(sys.argv[1],"r")
out_file = open(sys.argv[1].replace(".in.",".out."),"w")


#Number of test cases
nTest = int(in_file.readline().strip("\n"))

#Cycle over test cases
for n in range(nTest):
	
	#Read number of components
	nComponents = int(in_file.readline().strip("\n"))

	#Allocate numpy arrays
	v1 = np.array([ int(x) for x in in_file.readline().strip("\n").split(" ") ])
	v2 = np.array([ int(x) for x in in_file.readline().strip("\n").split(" ") ])

	#Compute the minimum scalar product
	min = minscalar(v1,v2)

	#Dump to destination file
	out_file.write("Case #{0}: {1}\n".format(n+1,min))

#Close file
in_file.close()
out_file.close()