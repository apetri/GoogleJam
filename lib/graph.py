import Queue

#Vertex types
UNDISCOVERED = 0
DISCOVERED = 1 
FINISHED = 2

#Vertex class
class Vertex(object):

	def __init__(self,key):
		self.key = key
		self.edges = set()
		self.state = UNDISCOVERED 

#Graph class
class Graph(object):

	def __init__(self,directed=False):
		
		#Book-keeping
		self._vertex_dict = dict()
		self._size = 0
		self._directed = directed
		self._parent = dict()

		#Entry/exit times
		self._time = 0
		self._entry_time = dict()
		self._exit_time = dict()

		#Finish dfs search
		self._finished = False 

	def __contains__(self,v):
		return v.key in self._vertex_dict

	def __iter__(self):
		for k in self._vertex_dict:
			yield self[k]

	def __getitem__(self,key):
		return self._vertex_dict[key] 

	@property
	def size(self):
		return self._size

	def add_vertex(self,v):

		assert isinstance(v,Vertex)

		if v in self:
			raise ValueError("Vertex {0} is already present!".format(v.key))

		#Add the vertex, increase the size of the graph
		self._vertex_dict[v.key] = v
		self._size += 1

	def add_edge(self,k1,k2):

		self[k1].edges.add(k2)
		if not self._directed:
			self[k2].edges.add(k1)


	#############################################
	###############Trasversal####################
	#############################################

	#Callbacks#

	def process_vertex_early(self,v):
		print("Process vertex {0} early".format(v.key))

	def process_vertex_late(self,v):
		print("Process vertex {0} late".format(v.key))

	def process_edge(self,v1,v2):
		print("Process edge {0}-->{1}".format(v1.key,v2.key))

	##################################################################################

	@property
	def parent(self):
		return self._parent

	@property
	def entry(self):
		return self._entry_time

	@property
	def exit(self):
		return self._exit_time

	def clear_search(self):
		
		self._parent = dict()
		self._time = 0
		self._entry_time = dict()
		self._exit_time = dict()

		for v in self:
			v.state = UNDISCOVERED

	#Breath first#
	def bfs(self,v):
		
		#Initialize the queue
		fifo = Queue.Queue()
		fifo.put(v)
		v.state = DISCOVERED

		#Start the breadth-first search from v
		while not fifo.empty():
			
			#Pop the vertex from the queue
			current_vertex = fifo.get()
			
			#Process vertex early
			self.process_vertex_early(current_vertex)

			#Process all the edges
			for edge in current_vertex.edges:

				target_vertex = self[edge]

				#Process the edge
				if (target_vertex.state!=FINISHED) or self._directed:
					self.process_edge(current_vertex,target_vertex)

				#Discover the new vertices
				if target_vertex.state==UNDISCOVERED:
					target_vertex.state = DISCOVERED
					fifo.put(target_vertex)
					self._parent[target_vertex.key] = current_vertex.key

			#Complete the vertex exploration
			current_vertex.state = FINISHED
			self.process_vertex_late(current_vertex)



	#Depth first#
	def dfs(self,v):

		#End the search 
		if self._finished:
			return 
		
		#Initialize the search
		v.state = DISCOVERED
		self.process_vertex_early(v)
		self._time+=1
		self._entry_time[v.key] = self._time

		#Process the edges
		for edge in v.edges:

			target_vertex = self[edge]
			
			if target_vertex.state==UNDISCOVERED:
				
				self._parent[target_vertex.key] = v.key
				self.process_edge(v,target_vertex)
				self.dfs(target_vertex)

			elif (target_vertex.state!=FINISHED and self._parent[v.key]!=target_vertex.key) or (self._directed):
				self.process_edge(v,target_vertex)
				if self._finished:
					return

		#Finish the search
		self.process_vertex_late(v)
		self._time+=1
		self._exit_time[v.key] = self._time
		v.state = FINISHED

