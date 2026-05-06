class Tree:
	def __init__(self):
		self.root = None
		self.nodes = []


	def get_node(self, value):
		for node in self.nodes:
			if node.value== value:
				return node
		
		return None

	def insert(self, treenode):
		self.nodes.append(treenode)

	
	def pre_trav(self):
		self.root.pre_trav()

	def in_trav(self):
		self.root.in_trav()


class TreeNode:
	def __init__(self, value):
		self.left_child = None
		self.right_child = None
		self.value = value 

	def set_left_child(self, left_child):
		self.left_child = left_child

	def set_right_child(self, right_child):
		self.right_child = right_child

	def pre_trav(self):
		print(self.value)
		if self.left_child != None:
			self.left_child.pre_trav()
		if self.right_child != None:
			self.right_child.pre_trav()

	def in_trav(self):
		if self.left_child != None:
			self.left_child.in_trav()
		print(self.value)
		if self.right_child != None:
			self.right_child.in_trav()

def main():
	num_nodes = int(input())

	tree = Tree()

	# tree.create_nodes(num_nodes)

	for i in range(num_nodes):

		str = input().split(" ")
		mid = str[0]
		left = str[1]
		right = str[2]

		if tree.get_node(mid) is None:
			treenode = TreeNode(mid)
			tree.insert(treenode)

		else: 
			treenode = tree.get_node(mid)

		if i == 0:
			tree.root = treenode

		if left != ".":
			if tree.get_node(left) is None:
				leftnode = TreeNode(left)
				tree.insert(leftnode)
			else:
				leftnode= tree.get_node(left)
			treenode.set_left_child(leftnode)


		if right != ".":
			if tree.get_node(right) is None:
				rightnode = TreeNode(right)
				tree.insert(rightnode)
			else:
				rightnode = tree.get_node(right)
			
			treenode.set_right_child(rightnode)
			

	# print(tree.get_tree_nodes())

	# for node in tree.get_tree_nodes():
	# 	print(node)

	# for node in tree.nodes:
	# 	print(f"left_child: {node.left_child}, right_child: {node.right_child}, value: {node.value}")

	# tree.pre_trav()
	tree.in_trav()


main()

				