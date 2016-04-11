#Toy implementation of a binary search tree in python

class BinaryTree(object):

	def __init__(self):
		
		self.root = None
		self.size = 0
		self.height = 0

	def __repr__(self):
		return "BinaryTree with {0} nodes of height {1}".format(self.size,self.height)

	@property
	def right(self):
		return self.root.right

	@property
	def left(self):
		return self.root.left 

	def insert(self,key,data=None):
		
		self.size += 1

		if self.root is None:
			self.root = TreeNode(key,data)
		else:
			self.height = self.root.insert(key,data)

		self.height = self.root.height

	def search(self,key):
		if self.root is None:
			return None
		else:
			return self.root.search(key)

	def compare(self,other):
		
		if (self.root is None)!=(other.root is None):
			return False

		if self.root is None:
			return True

		return self.root.compare(other.root)

	def isValid(self):
		return self.root.isValid()


class TreeNode(object):

	def __init__(self,key,data=None):

		self.key = key
		self.data = data
		self.parent = None
		self.left = None
		self.right = None
		self.height = 1

	def __repr__(self):
		return "SubTree of height {0}".format(self.height)

	def insert(self,key,data=None):

		if key<self.key:
			
			if self.left is None:
				self.left = self.__class__(key,data)
				self.left.parent = self
				height = 1
			else:
				height = self.left.insert(key,data) + 1
				if height>self.height:
					self.height = height
				return height

		else:

			if self.right is None:
				self.right = self.__class__(key,data)
				self.right.parent = self
				height = 1
			else:
				height = self.right.insert(key,data) + 1

		if height+1>self.height:
			self.height = height+1

		return height


	def search(self,key):

		if key==self.key:
			return self
		elif key<self.key:
			if self.left is None:
				return None
			else:
				return self.left.search(key)
		else:
			if self.right is None:
				return None
			else:
				return self.right.search(key)

	def compare(self,other):

		if self.key!=other.key:
			return False

		if (self.left is None)!=(other.left is None):
			return False

		if (self.right is None)!=(other.right is None):
			return False

		if (self.left is None) and (self.right is None):
			return True

		if self.left is None:
			return self.right.compare(other.right)

		if self.right is None:
			return self.left.compare(other.left) 

		return self.left.compare(other.left) and self.right.compare(other.right)

	def isValid(self):
		raise NotImplementedError








	
