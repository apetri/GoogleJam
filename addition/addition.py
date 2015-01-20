from __future__ import division

import sys
from graph_tool.all import Graph,dfs_search,DFSVisitor,shortest_path,graph_draw

#Parse input strings
def parseLine(line):

	left,right = line.split("=")
	value = int(right)
	first,second = left.split("+")

	return first,second,value

def parseQuestion(line):

	return line.split("+")

#Build the graph given the known conditions (each one is an edge)
def parseGraph(conditions):

	#Hash table that maps names to vertices
	vertex = dict()
	count = 0

	#Graph
	g = Graph(directed=False)

	#Name of the vertices
	name = g.new_vertex_property("string")
	g.vertex_properties["name"] = name

	#Numerical value of the vertices
	value = g.new_vertex_property("float")
	g.vertex_properties["value"] = value

	#Color of the vertices
	color = g.new_vertex_property("string")
	g.vertex_properties["color"] = color

	#Parent of this vertex during DFS
	parent = g.new_vertex_property("object")
	g.vertex_properties["parent"] = parent

	#Weight of the edges
	weight = g.new_edge_property("int")
	g.edge_properties["weight"] = weight

	#Is an edge tree or back
	tree = g.new_edge_property("bool")
	g.edge_properties["tree"] = tree

	#Cycle over all the conditions
	for condition in conditions:
		n1,n2,v = parseLine(condition)

		#Add the vertices if not there already
		for n in [n1,n2]:
			try:
				vertex[n]
			except KeyError:
				vertex[n] = count
				count += 1
				new_vertex = g.add_vertex()
				name[new_vertex] = n
				color[new_vertex] = "grey"
				parent[new_vertex] = None
				value[new_vertex] = 0

		#Add the edge if not there already
		if g.edge(vertex[n1],vertex[n2]) is None:
			new_edge = g.add_edge(vertex[n1],vertex[n2])
			weight[new_edge] = v
			tree[new_edge] = False

	#The graph is built, return
	return g,vertex


#Color the graph during DFS using the ColorVisitor class 
class ColorVisitor(DFSVisitor):

	def __init__(self,graph):
		self.graph = graph
		self.blue = False
		self.propagate = False

	def togglePropagate(self):
		self.propagate = not(self.propagate)

	def finish_vertex(self,u):
		if self.blue:
			self.graph.vertex_properties["color"][u]="blue"

	def start_vertex(self,u):
		if self.graph.vertex_properties["color"][u]=="grey":
			self.graph.vertex_properties["color"][u]="black"

	def tree_edge(self,e):
		
		if not self.propagate:
		
			#Mark the edge as tree
			self.graph.edge_properties["tree"][e] = True

			source_color = self.graph.vertex_properties["color"][e.source()]
		
			if source_color=="red":
				target_color="black"
			elif source_color=="black":
				target_color="red"
			elif source_color=="blue":
				target_color="blue"
		
			self.graph.vertex_properties["color"][e.target()] = target_color

			#Determine the parenthood chain
			child = e.target()
			parent = e.source()
			self.graph.vertex_properties["parent"][child] = parent

		else:
			targetName = self.graph.vertex_properties["name"][e.target()]
			targetValue = self.graph.edge_properties["weight"][e] - self.graph.vertex_properties["value"][e.source()]
			self.graph.vertex_properties["value"][e.target()] = targetValue
			self.graph.vertex_properties["name"][e.target()] = "{0}={1:.1f}".format(targetName,targetValue)


	def back_edge(self,e):

		#Execute only if the edge is a back edge
		if not(self.graph.edge_properties["tree"][e]) and not(self.blue):
			if self.graph.vertex_properties["color"][e.source()]==self.graph.vertex_properties["color"][e.target()]:
				
				#Color vertices in blue
				self.graph.vertex_properties["color"][e.source()]="blue"
				self.graph.vertex_properties["color"][e.target()]="blue"
				self.blue=True

				#We know exactly the value of the vertex at this point
				targetName = self.graph.vertex_properties["name"][e.target()]
				targetValue = (self.graph.edge_properties["weight"][e] + computePath(self.graph,e.target(),e.source())) / 2
				self.graph.vertex_properties["value"][e.target()] = targetValue
				self.graph.vertex_properties["name"][e.target()] = "{0}={1:.1f}".format(targetName,targetValue)
				self.start = e.target()



#Sum the values of the edges, alternating signs, along a path
def computePath(g,source,target):

	value = 0
	sign = -1

	while source!=target:
		parent = g.vertex_properties["parent"][target]
		value += sign*g.edge_properties["weight"][g.edge(parent,target)]
		target = parent
		sign *= -1

	return value

#Given the question asked, decide if we can answer it
def answerQuestion(g,vertex,n1,n2):

	#Translate the names into the corresponding vertices
	try:
		u1 = g.vertex(vertex[n1])
		u2 = g.vertex(vertex[n2])
	except KeyError:
		return None

	########################	
	##Now the fun begins####
	########################

	if g.edge(u1,u2) is not None:

		#If there is an edge between these two vertices, the weight is the answer
		answer = g.edge_properties["weight"][g.edge(u1,u2)]

	elif (g.vertex_properties["color"][u1]=="blue") and (g.vertex_properties["color"][u2]=="blue"):

		#If the two vertices are blue, we know exactly their value
		answer = g.vertex_properties["value"][u1] + g.vertex_properties["value"][u2]

	elif g.vertex_properties["color"][u1]!=g.vertex_properties["color"][u2]:

		#If the two verices have a different color, there might still be hope, if they are in the same connected component
		vertices_path,edges_path = shortest_path(g,u1,u2)

		#If there is no path, forget it
		if len(edges_path)==0:
			return None

		#Otherwise we can compute an answer
		sign = 1
		answer = 0

		#Sum the values of the edges with alternate signs
		for edge in edges_path:
			answer += sign * g.edge_properties["weight"][edge]
			sign *= -1

		#Check that we did everything correctly
		assert sign==-1

		#We know the answer, it means our graph has a new black-red edge now
		edge = g.add_edge(u1,u2)
		g.edge_properties["weight"][edge] = answer

	else:
		return None

	#We have the answer now, format it into a string
	return "{0}+{1}={2}".format(n1,n2,int(answer))


if __name__=="__main__":

	#In/out filenames
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")
	outfile = open(output_filename,"w")

	#Cycle over input lines
	with open(input_filename,"r") as infile:

		#Get number of test cases
		nTest = int(infile.readline().rstrip("\n"))

		#Cycle over test cases
		for t in range(nTest):

			print("Processing case {0}...".format(t+1))
			outfile.write("Case #{0}:\n".format(t+1))

			#Read in number of conditions
			nConditions = int(infile.readline().rstrip("\n"))

			#Read in all the conditions
			conditions = list()
			for n in range(nConditions):
				conditions.append(infile.readline().rstrip("\n"))

			#Build a graph with the conditions
			print("Building the graph...")
			g,vertex = parseGraph(conditions)

			#Proceed in the graph coloring, making sure we get all the connected components
			print("Coloring the graph...")
			for v in g.vertices():
				if g.vertex_properties["color"][v]=="grey":

					colvis = ColorVisitor(g)
					dfs_search(g,v,visitor=colvis)

					#If the component is solvable, solve it
					if g.vertex_properties["color"][v]=="blue":
						colvis.togglePropagate()
						dfs_search(g,colvis.start,visitor=colvis)

			#Draw the colored graph
			#print("Drawing the graph...")
			#graph_draw(g,vertex_text=g.vertex_properties['name'],edge_text=g.edge_properties['weight'],vertex_fill_color=g.vertex_properties['color'],output='small{0}.png'.format(t+1),vertex_font_size=18,edge_font_size=18)

			#The graph is colored, read the questions
			nQuestions = int(infile.readline().rstrip("\n"))

			#Cycle over the questions, answer them and write the answers to the output
			print("Answering questions...")
			for n in range(nQuestions):
				question = infile.readline().rstrip("\n")
				n1,n2 = parseQuestion(question)
				answer = answerQuestion(g,vertex,n1,n2)
				if answer is not None:
					outfile.write("{0}\n".format(answer))


	#Close output file
	outfile.close()






		
	



