import Queue

class MinHeap(object):
	
	def __init__(self,*args,**kwargs):
		self._queue = Queue.PriorityQueue(*args,**kwargs)

	def put(self,priority,data):
		self._queue.put((priority,data))

	def get(self):
		if self._queue.empty():
			return None
		return self._queue.get()

	@property
	def queue(self):
		return self._queue.queue

	@property
	def empty(self):
		return self._queue.empty()


class MaxHeap(object):
	
	def __init__(self,*args,**kwargs):
		self._queue = Queue.PriorityQueue(*args,**kwargs)

	def put(self,priority,data):
		self._queue.put((-priority,data))

	def get(self):
		if self._queue.empty():
			return None
		item = self._queue.get()
		return (-item[0],item[1])

	@property
	def queue(self):
		return [ (-item[0],item[1]) for item in self._queue.queue]

	@property
	def empty(self):
		return self._queue.empty()