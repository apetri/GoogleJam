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

	def callback_null(self):
		return None

	def inorder(self,with_null=False):

		collect = list()

		if self.left is not None:
			collect += self.left.inorder(with_null)

		if self.left is None and with_null:
			collect.append(self.callback_null())

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		if self.right is not None:
			collect += self.right.inorder(with_null)

		if self.right is None and with_null:
			collect.append(self.callback_null())

		return collect


	def preorder(self,with_null=False):
		
		collect = list()

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		if self.left is not None:
			collect += self.left.preorder(with_null)

		if self.left is None and with_null:
			collect.append(self.callback_null())

		if self.right is not None:
			collect += self.right.preorder(with_null)

		if self.right is None and with_null:
			collect.append(self.callback_null())

		return collect


	def postorder(self,with_null=False):

		collect = list()

		if self.left is not None:
			collect += self.left.postorder(with_null)

		if self.left is None and with_null:
			collect.append(self.callback_null())

		if self.right is not None:
			collect += self.right.postorder(with_null)

		if self.right is None and with_null:
			collect.append(self.callback_null())

		callback_result = self.callback_node()
		if callback_result is not None:
			collect.append(callback_result)

		return collect

	#Build the tree from preorder and inorder trasversal sequences (no data stored)
	@classmethod
	def build_from_trasversal(cls,preorder=[],inorder=[],pl=0,pr=None,il=0,ir=None,lookup=None):

		#Safety check
		if len(preorder)!=len(inorder):
			raise ValueError("Preorder and inorder sequences must have the same length")

		#Fill values and lookup table
		if pr is None:
			pr = len(preorder)

		if ir is None:
			ir = len(inorder)

		if lookup is None:
			lookup = dict([(k,n) for n,k in enumerate(inorder)])

		#If the lists are empty there is nothing to do
		if pl>=pr:
			return None

		#The first entry in the preorder is the root
		root = cls(preorder[pl])
		root_index_inorder = lookup[root.key]

		#Reconstruct the right and left subtrees
		root.left = cls.build_from_trasversal(preorder,inorder,pl=pl+1,pr=pl+1+root_index_inorder-il,il=il,ir=root_index_inorder,lookup=lookup)
		root.right = cls.build_from_trasversal(preorder,inorder,pl=pl+1+root_index_inorder-il,pr=pr,il=root_index_inorder+1,ir=ir,lookup=lookup)

		#Return
		return root 





	
