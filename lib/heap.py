from __future__ import division

from abc import ABCMeta,abstractproperty,abstractmethod
import numpy as np

#####################
#Abstract heap class#
#####################

class Heap(object):

	__metaclass__ = ABCMeta

	#Heap property comparison method is abstract
	@abstractmethod
	def compare(a,b):
		pass

	#Constructor
	def __init__(self,maxSize=100):
		self._queue = np.empty(maxSize,dtype=HeapNode)
		self._size = 0

	#Heap size
	@property
	def size(self):
		return self._size

	#Empty or not
	@property
	def empty(self):
		return not(self._size)

	#First element 
	def top(self,retrieve_data=True):
		if not(self.size):
			raise ValueError("Heap is empty!!")

		if retrieve_data:
			return self._queue[1].key,self._queue[1].data
		else:
			return self._queue[1].key

	###################
	#Heap construction#
	###################

	#Parent 
	def _parent(self,n):
		if n==1:
			return None
		else:
			return n//2

	#First child
	def _child(self,n):
		return 2*n

	#Bubble up method
	def _bubble_up(self,n):

		parent = self._parent(n)

		#We are at the top, nothing to do
		if parent is None:
			return

		#Recursive bubble up
		if self.compare(self._queue[n],self._queue[parent]):
			self._queue[n],self._queue[parent] = self._queue[parent],self._queue[n]
			self._bubble_up(parent)

	#Bubble down method
	def _bubble_down(self,n):
		
		child = self._child(n)
		min_index = n

		for i in (0,1):
			if (child+i<=self.size) and (self.compare(self._queue[child+i],self._queue[min_index])):
				min_index = child+i

		if min_index!=n:
			self._queue[min_index],self._queue[n] = self._queue[n],self._queue[min_index]
			self._bubble_down(min_index)
	
	###########
	#Insertion#
	###########

	def put(self,key,data=None):

		#Construct node
		node = HeapNode(key,data)

		#Place in the heap
		self._size+=1
		self._queue[self.size] = node
		self._bubble_up(self.size)

	################# 
	#Pop top element#
	#################

	def get(self,retrieve_data=True):

		#If empty return nothing
		if self.empty:
			return None

		#Retrieve first element
		self._queue[1],self._queue[self.size] = self._queue[self.size],self._queue[1]
		self._size-=1
		self._bubble_down(1)

		#Return to user
		node = self._queue[self.size+1]

		if retrieve_data:
			return node.key,node.data
		else:
			return node.key 

###########
#Data node#
###########

class HeapNode(object):

	def __init__(self,key,data=None):
		self.key = key
		self.data = data


#############################################################
#############################################################

######################################
#MinHeap: smallest element at the top#
######################################

class MinHeap(Heap):
	
	def compare(self,a,b):
		return a.key<b.key

class MaxHeap(Heap):
	
	def compare(self,a,b):
		return a.key>b.key