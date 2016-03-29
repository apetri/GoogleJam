import sys

from graph_tool.all import Graph
from graph_tool.search import bfs_search,BFSVisitor

#Connected component size counter

class ComponentSize(BFSVisitor):

	def __init__(self):
		self._component_size = 0

	def discover_vertex(self,u):
		self._component_size += 1

	@property
	def component_size(self):
		return self._component_size


#Parse input into a graph

def parse_graph(following,n):

	g = Graph()

	#Add n vertices to the graph
	g.add_vertex(n)

	#Add a directed edge from a monk to each of his followers
	for i,j in enumerate(following):
		g.add_edge(g.vertex(int(j)-1),g.vertex(i))


	#Return the created graph
	return g


#Main execution

if __name__=="__main__":

	#Input and output filenames
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")

	#Output file descriptor
	output = file(output_filename,"w")

	#Process the input one case at a time
	with open(input_filename,"r") as infile:

		nTest = int(infile.readline().rstrip("\n"))
		
		for t in range(nTest):

			#Case header
			output.write("Case #{0}:\n".format(t+1))

			#Parse the number of monks
			nMonks = int(infile.readline().rstrip("\n"))

			#Build the graph
			following = infile.readline().rstrip("\n").split(" ")
			g = parse_graph(following,nMonks)

			#For each monk, compute the size of the connected component the monk sits in, using breath-first search
			for m in range(nMonks):
				counter = ComponentSize()
				bfs_search(g,g.vertex(m),visitor=counter)
				output.write("{0}\n".format(counter.component_size))


	#Close output file
	output.close()