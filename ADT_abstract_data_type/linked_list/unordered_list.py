from node import Node
class UnorderedList:
	"""
	a class used to represent an Unordered List (Linked List)
	attributes:
	------------
	head: Node
		The head (first element) of the linked list
	node_count: int
		The number of nodes in the linked list

	Methods:
	-------------
	is_empty(): Checks if the linked list is empty
	add(item): Adds an item to the front of the list.
	size(): Returns the size of the linked list
	search(item): Searches for an item in the linked list
	remove(item): Removes the first occurrence of an item in the linked list
	"""
	def __init__(self):
		"""
		Initializes an empty linked list.
		"""
		self.head = None
		self.node_count = 0

	def is_empty(self):
		"""
		Check if the list is empty.
		@return: boolean value
		"""
		return self.head is None

	def add(self, item):
		"""
		Adds an item to the front of the list.
		@param item: The item to be added to the front of the list.
		"""
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp
		self.node_count += 1

	def size(self):
		"""
		Get the number of nodes in the linked list.
		@return: int value
		"""
		return self.node_count

	def search(self, item):
		"""
		Search for an item in the linked list.
		@param item
		@return: boolean value
		"""
		current = self.head
		found = False
		while current is not None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()
		return found

	def remove(self, item):
		"""
		Remove the first occurrence of an item in the linked list.
		@param item
		"""
		current = self.head
		previous = None
		found = False
		while not found:
			if current is None:
				raise ValueError("Node does not exist")
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
		# decrease the count
		self.node_count -= 1