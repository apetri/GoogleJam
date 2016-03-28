#!/usr/bin/env python

import sys

class DirectoryTree(object):

	def __init__(self):
		self.root = dict()

	#Add a directory to the path
	def mkdir(self,path):

		#Split path into single directories
		directories = path.split("/")[1:]

		#Initial step
		node = self.root
		nof_mkdir = 0

		#Cycle over directories 
		for d in directories:
			if not (d in node):
				#Create a directory
				node[d] = dict()
				nof_mkdir += 1

			#Walk on the next node
			node = node[d]

		#Return the number of mkdir to the user
		return nof_mkdir

#####################
#########Main########
#####################

line = lambda : sys.stdin.readline().strip("\n")

def main():

	#Number of test cases
	ntest = int(line())

	#Cycle over test cases
	for t in range(ntest):

		#Read N,M
		n,m = [int(c) for c  in line().split(" ")]

		#Add the N directories to the directory tree data structure
		tree = DirectoryTree()
		for i in range(n):
			path = line()
			tree.mkdir(path)

		#Create the M directories, keeping track of the number of mkdir commands
		nof_mkdir = 0
		for i in range(m):
			path = line()
			nof_mkdir += tree.mkdir(path)
		
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,nof_mkdir))

if __name__=="__main__":
	main()