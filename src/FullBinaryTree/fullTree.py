#!/usr/bin/env python
from __future__ import division
import sys

import numpy as np
from lib import graph as gph

#Subclass from graph library
class TreeNode(gph.Vertex):

	def __init__(self,key):
		super(TreeNode,self).__init__(key)
		self.subtree_size = None
		self.max_nodes_in_subtrees = None
		self.max_nodes_in_subtrees = 0

class SubTreeVisitor(gph.Visitor):

	#Trasversal callbacks
	def process_vertex_early(self,g,v):
		v.subtree_size = list()

	def process_vertex_late(self,g,v):

		#Consider the case in which this is a leaf
		if (len(v.subtree_size) in [0,1]):
			v.max_nodes_in_subtrees = 0

			if v.key in self.parent:
				g[self.parent[v.key]].subtree_size.append(1+v.max_nodes_in_subtrees)

			return

		#If it is not a leaf then select the two largest subtree lengths (if only one do nothing)
		v.subtree_size.sort()
		v.max_nodes_in_subtrees = v.subtree_size[-1]+v.subtree_size[-2]
		
		if v.key in self.parent:
			g[self.parent[v.key]].subtree_size.append(1+v.max_nodes_in_subtrees)
 
	def process_edge(self,g,v1,v2):
		pass

###############################################################################################

def minDeletions(source,destination,N):

	#Create the graph
	g = gph.Graph()
	for n in range(N-1):
		v1,v2 = TreeNode(source[n]),TreeNode(destination[n])
		
		for v in (v1,v2):
			try:
				g.add_vertex(v)
			except ValueError:
				pass

		g.add_edge(source[n],destination[n])

	#Perform a DFS for each choice of the root (quadratic algorithm)
	max_nodes = 0
	for v in g:

		visitor = SubTreeVisitor(g,v)
		visitor.dfs()
		
		if v.max_nodes_in_subtrees+1>max_nodes:
			max_nodes = v.max_nodes_in_subtrees+1

	#Return
	return N-max_nodes

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
		
		#Read N
		N = getint()
		source = np.zeros(N-1,dtype=np.int)
		destination = np.zeros_like(source)

		#Read in the edges
		for n in range(N-1):
			source[n],destination[n] = getintlist()

		#Calculate answer and output
		sys.stdout.write("Case #{0}: {1}\n".format(t+1,minDeletions(source,destination,N)))

if __name__=="__main__":
	main()