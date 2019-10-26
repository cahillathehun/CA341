
"""
Implement a program that provides the following operations on a binary tree.
	insert adds an integer x into a binary tree T to give a binary tree R.
	search returns true if x is contained in the binary tree T.
	preorder lists the nodes of the binary tree T using preorder traversal.
	inorder lists the nodes of the binary tree T using inorder traversal.
	postorder lists the nodes of the binary tree T using postorder traversal.
"""

class BinaryNode:
	#BinaryNode class.
	#Each Binary node has:
	#	-value
	#	-left
	#	-right
	#both left and right set to None.

	def __init__(self, val):
		#func to intialise BinaryNode
		self.val = val
		self.left = None
		self.right = None

	def __str__(self):
		#Not actually used because we're never printing the node,
		#only print things using BinaryTree class methods.
		return "{} is in this node".format(self.val)

class BinaryTree:
	#class for the Binary Tree.
	#Only 1 created in the main,
	#called "Tree".
	def __init__(self):
		self.root_node = None

	"""
	This method not needed because we print the BinaryTree with:
		-pre_order()
		-in_order()
		-post_order()

	def __str__(self):
		return str(self.root_node)
		pass
	"""

	def makeRoot(self, val):
		#sets the root node
		self.root_node = BinaryNode(val)

	def insert(self,val):
		#checks if root is None and insert if it is otherwise go through the tree
		if not self.root_node:
			#make val the root
			self.makeRoot(val)
		else:
			#root_node not empty -> call insertNode
			self.insertNode(self.root_node,val)

	def insertNode(self, node, val):
		#adds integer "val" into the Tree T, giving Binary Tree R
		if val < node.val:
			#check if node.left is empty
			if node.left:
				#node.left is'nt empty -> call function again
				self.insertNode(node.left, val)
			else:
				#node.left is empty -> add val
				node.left = BinaryNode(val)
				print("Node added!(on left)")
		else:
			#check if node.right is empty
			if node.right:
				#node.right is'nt empty -> call function again
				self.insertNode(node.right, val)
			else:
				#node.right is empty -> add val
				node.right = BinaryNode(val)
				print("Node added!(on right)")

	def search(self, val):
		#call this instead of having node.self.root_node everytime in "searchForNode()"
		return self.searchForNode(self.root_node, val)

	def searchForNode(self, node, val):
		#returns True if int(x) is in the Tree
		if not node:
			#nothing in the root_node
			print("False")
			return False
		elif node.val == val:
			#node found
			print("True")
			return True
		elif val < node.val:
			#val bigger than current node val, search node.left
			return self.searchForNode(node.left, val)
		elif val > node.val:
			#val smaller than current node val, search node.right
			return self.searchForNode(node.right, val)
		else:
			#node not found
			print("False")
			return False

	def pre_order(self, node):
		#lists nodes of Tree using preorder traversal
		if node:
			print(node.val)
			self.pre_order(node.left)
			self.pre_order(node.right)

	def in_order(self, node):
		#lsits nodes of Tree using inorder traversal
		if node:
			self.in_order(node.left)
			print(node.val)
			self.in_order(node.right)

	def post_order(self, node):
		#lists nodes of Tree using postorder traversal
		if node:
			self.post_order(node.left)
			self.post_order(node.right)
			print(node.val)


def main():

	Tree = BinaryTree()
	cmd = str(input("Commands are: \n" + "'i' to insert an integer. \n" +
			"'s' to search for an integer\n" +
			"'pre' to list the nodes using preorder traversal\n" +
			"'inorder' to list the nodes using inorder traversal\n" +
			"'post' to list the nodes using postorder traversal \n"))

	Tree.insert(27)		#<---+
	Tree.insert(14)		#    |
	Tree.insert(35)		#    |
	Tree.insert(10)		#All for testing
	Tree.insert(19)		#    |
	Tree.insert(31)		#    |
	Tree.insert(42)		#<---+

	while cmd != "q":
		if cmd == "i":
			val = int(input("please enter a value(int)"))
			if isinstance(val,int):  #<-- checks if val is an int
				print("Adding node!")
				#insert val into Treeeeeeee
				Tree.insert(val)
			else:
				print(val, "is not a valid integer.\n")
		elif cmd == "s":
			val = int(input("Please input an integer to search for"))
			#search for val in Tree
			Tree.search(val)
		elif cmd == "pre":
			#call pre_order() on Tree
			node = Tree.root_node
			Tree.pre_order(node)
		elif cmd == "inorder":
			#call in_order() on Tree
			node = Tree.root_node
			Tree.in_order(node)
		elif cmd == "post":
			#call post_order() on Tree
			node = Tree.root_node
			Tree.post_order(node)
		else:
			print("Command not recognised.\n")

		cmd = str(input("Commands are:\n" + "'i' to insert an integer.\n" +
				"'s' to search for an integer\n" +
				"'pre' to list the nodes using preorder traversal\n" +
				"'inorder' to list the nodes using inorder traversal\n" +
				"'post' to list the nodes using postorder traversal\n"))

if __name__ == "__main__":
	print("Starting BST program!\n")
	main()
