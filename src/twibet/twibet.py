#!/usr/bin/env python
from __future__ import division
import sys

import lib.graph as gph

sys.setrecursionlimit(10000)

###################
##Graph utilities##
###################

TREE = 0
CYCLE = 1

class Monk(gph.Vertex):

	def __init__(self,key):
		super(Monk,self).__init__(key)
		self.cc_size = 1
		self.path_length = 1
		self.type = TREE
		self.cycle_number = None

class CycleVisitor(gph.Visitor):

	def __init__(self,g,v):
		super(CycleVisitor,self).__init__(g,v)
		self.cycle_number = 0
		self.add_to_cycle = dict()

	def process_vertex_early(self,g,v):
		pass

	def process_vertex_late(self,g,v):

		if v.type==CYCLE and (v.key in self.parent):
			parent_vertex = g[self.parent[v.key]] 
			parent_vertex.type = CYCLE 
			parent_vertex.cc_size = v.cc_size
			parent_vertex.cycle_number = v.cycle_number


	def process_edge(self,g,v1,v2):
		
		if v2.state==gph.UNDISCOVERED:
			v2.path_length = v1.path_length + 1

		if v2.state==gph.DISCOVERED:
			v1.type = CYCLE
			v1.cycle_number = self.cycle_number
			self.add_to_cycle[v1.cycle_number] = 0
			v1.cc_size = v1.path_length

class TreeVisitor(gph.Visitor):

	def process_vertex_early(self,g,v):
		pass

	def process_vertex_late(self,g,v):
		for target in v.edges:
			v.cc_size += g[target].cc_size

	def process_edge(self,g,v1,v2):
		pass

#########################################

def whisper(N,follows):
	
	#Parse graph
	g = gph.Graph(directed=True)
	for n in range(N):
		g.add_vertex(Monk(n))

	for n in range(N):
		g.add_edge(follows[n]-1,n)

	#Depth first search to find cycles
	cyclevisitor = CycleVisitor(g,g[0])
	for n in range(N):
		if g[n].state==gph.UNDISCOVERED:
			cyclevisitor.cycle_number += 1
			cyclevisitor.set_source(g[n])
			cyclevisitor.dfs()

	#Depth first search to find trees
	treevisitor = TreeVisitor(g,g[0])
	for n in range(N):
		if g[n].state==gph.UNDISCOVERED and g[n].type==TREE:
			treevisitor.set_source(g[n])
			treevisitor.dfs()

	#See if any trees attach to the cycles
	for v in g:
		if v.type==CYCLE:
			for target in v.edges:
				if g[target].type==TREE:
					cyclevisitor.add_to_cycle[v.cycle_number] += g[target].cc_size 

	#Return component sizes with cycles added
	cc_sizes = list()
	for n in range(N):
		if g[n].type==TREE:
			cc_sizes.append(g[n].cc_size)
		else:
			cc_sizes.append(g[n].cc_size + cyclevisitor.add_to_cycle[g[n].cycle_number])

	return cc_sizes

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
		follows = getintlist()
		whispers = whisper(N,follows)

		#Calculate answer and output
		sys.stdout.write("Case #{0}:\n".format(t+1))
		for n in range(N):
			sys.stdout.write("{0}\n".format(whispers[n]))

if __name__=="__main__":
	main()