#!/usr/bin/env python
from __future__ import division
import sys

import lib.graph as gph

#Colors
UNDECIDED = None
RED = 1
BLACK = -1

#Recursion depth
sys.setrecursionlimit(100000)

##########################################################################

#Vertex type
class Variable(gph.WeightedVertex):

	def __init__(self,key):

		super(Variable,self).__init__(key)
		self.color = UNDECIDED
		self.value = None
		self.component = None
		self.cumulated_path = 0

###########################################################################

#Coloring visitor
class ColorFill(gph.Visitor):

	def __init__(self,g,v):
		super(ColorFill,self).__init__(g,v)
		self.component_known = dict()

	def process_vertex_early(self,g,v):
		pass

	def process_vertex_late(self,g,v):
		pass

	def process_edge(self,g,v1,v2):
		
		#If we are discovering the vertex
		if v2.state==gph.UNDISCOVERED:

			#Connected component and color
			v2.component = v1.component
			v2.color = -v1.color
			v2.cumulated_path = v1.cumulated_path + v1.color*v1.weight(v2)

		else:
			
			#If the vertex is already discovered and they are the same color
			if v1.color==v2.color:
				v2.value = (v1.weight(v2) + v1.color*(v1.cumulated_path - v2.cumulated_path)) / 2 
				self.component_known[v2.component] = v2

#Fill value visitor
class ValueFill(gph.Visitor):

	def process_vertex_early(self,g,v):
		pass

	def process_vertex_late(self,g,v):
		pass

	def process_edge(self,g,v1,v2):
		
		if v2.state==gph.UNDISCOVERED:
			v2.value = v1.weight(v2) - v1.value

########################################################################################################

def calculateAnswers(N,known,Q,questions):

	#Answer list
	answers = list()

	#Parse the known answers in a graph
	g = gph.WeightedGraph()
	for ans in known:

		addends,value = ans.split("=")
		k1,k2 = addends.split("+")

		#Vertices
		for k in (k1,k2):
			var = Variable(k)
			if var not in g:
				g.add_vertex(var)

		#Edges
		g.add_edge(k1,k2,int(value))

	#Do a first DFS to color the graph
	colorfill = ColorFill(g,g[k])
	component = 0
	for v in g:
		
		if v.state==gph.UNDISCOVERED:	
			component += 1
			v.component = component 
			v.color = RED
			colorfill.set_source(v)
			colorfill.dfs()

	#Do a second DFS to fill in the known values of the variables
	valuefill = ValueFill(g,g[k])
	for cc in colorfill.component_known:
		valuefill.set_source(colorfill.component_known[cc])
		valuefill.dfs()

	#########################################
	#############Ready to answer#############
	#########################################

	for question in questions:

		#Parse question
		k1,k2 = question.split("+")

		#Check that we have information on (k1,k2)
		try:
			g[k1]
		except KeyError:
			continue

		try:
			g[k2]
		except KeyError:
			continue

		#If we have value info on both k1,k2 we can answer
		if (g[k1].value is not None) and (g[k2].value is not None):
			answer_value = int(g[k1].value+g[k2].value)
			answers.append(question+"={0}".format(answer_value))
			continue

		#If we do not have value info, there needs to be a path between k1 and k2
		if g[k1].component!=g[k2].component:
			continue

		#If there exists a path between k1,k2, they need to have different colors
		if g[k1].color==g[k2].color:
			continue

		if k2 in g[k1].edges:
			answers.append(question+"={0}".format(g[k1].weight(g[k2])))
			continue

		#Reconstruct the paths to the root
		answer_value = -int(g[k1].cumulated_path*g[k1].color + g[k2].cumulated_path*g[k2].color)
		answers.append(question+"={0}".format(answer_value))

	#Return
	return answers


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
		
		#Parse known answers and questions
		known = list()
		questions = list()
		
		N = getint()
		for n in range(N):
			known.append(line())

		Q = getint()
		for q in range(Q):
			questions.append(line())

		#Answers
		answers = calculateAnswers(N,known,Q,questions)

		#Calculate answer and output
		sys.stdout.write("Case #{0}:\n".format(t+1))
		sys.stdout.write("\n".join(answers)+"\n")

if __name__=="__main__":
	main()