#Toy implementation of a binary search tree in python

#####################################################################
#####################################################################

class TreeNode(object):

	def __init__(self,key,data=None):

		self.key = key
		self.data = data
		self.parent = None
		self.left = None
		self.right = None
		self.height = 0
		self.size = 1

	def __repr__(self):
		return "Tree of height {0}, with {1} elements".format(self.height,self.size)

	def insert(self,key,data=None):

		self.size+=1

		if key<self.key:
			
			if self.left is None:
				self.left = self.__class__(key,data)
				self.left.parent = self
				height = 1
			else:
				height = self.left.insert(key,data) + 1

		else:

			if self.right is None:
				self.right = self.__class__(key,data)
				self.right.parent = self
				height = 1
			else:
				height = self.right.insert(key,data) + 1

		if height>self.height:
			self.height = height

		return height


	#################################
	###########Search################
	#################################

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

	#################################
	###########Compare###############
	#################################

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

	############################################
	###########Valid search tree################
	############################################

	def isValid(self):
		raise NotImplementedError

	#################################
	###########Trasversal############
	#################################

	def callback_node(self):
		return self.key

	def inorder(self):

		collect = list()

		if self.left is not None:
			collect += self.left.inorder()

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		if self.right is not None:
			collect += self.right.inorder()

		return collect


	def preorder(self):
		
		collect = list()

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		if self.left is not None:
			collect += self.left.preorder()

		if self.right is not None:
			collect += self.right.preorder()

		return collect


	def postorder(self):

		collect = list()

		if self.left is not None:
			collect += self.left.postorder()

		if self.right is not None:
			collect += self.right.postorder()

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		return collect

	#Build the tree from preorder and inorder trasversal sequences (no data stored)
	@classmethod
	def build_from_trasversal(cls,preorder=[],inorder=[]):

		#Safety check
		if len(preorder)!=len(inorder):
			raise ValueError("Preorder and inorder sequences must have the same length")

		#If the lists are empty there is nothing to do
		if not(len(preorder)):
			return None

		#The first entry in the preorder is the root
		root = cls(preorder[0])
		root_index_inorder = inorder.index(preorder[0])

		#Reconstruct the right and left subtrees
		root.left = cls.build_from_trasversal(preorder=preorder[1:root_index_inorder+1],inorder=inorder[:root_index_inorder])
		root.right = cls.build_from_trasversal(preorder=preorder[root_index_inorder+1:],inorder=inorder[root_index_inorder+1:])

		#Return
		return root 





	
