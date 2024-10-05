from node import Node
class UnorderedList:
	"""
	a class used to represent an Unordered List (Linked List)
	attributes:
	------------
	head: Node
		The head (first element) of the linked list
	tail : Node
		the tail (last element) of the linked list
	node_count: int
		The number of nodes in the linked list

	Methods:
	-------------
	is_empty():
		Checks if the linked list is empty
	add(item):
		Adds an item to the front of the list.
	size():
		Returns the size of the linked list
	search(item):
		Searches for an item in the linked list
	remove(item):
		Removes the first occurrence of an item in the linked list
	append(item):
		Append an item to the end of the linked list.
	insert(position, item):
		Insert an item at the front of the linked list.
	index(item):
		Returns the index of the first occurrence of an item in the linked list.
	slicing(start, stop):
		Returns a new list containing the items from start to stop indices. Don't count the item in stop position. (like a list)
	reverse():
		Reverses the linked list in place. In-place.
	"""
	def __init__(self):
		"""
		Initializes an empty linked list.
		"""
		self.head = None
		self.tail = None
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
		if temp.get_next() is None:  #First node, so it's both head and tail
			self.tail = temp
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
		while not found and current is not None:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()
		if found:
			if previous is None: #removing the head
				self.head = current.get_next()
				if self.head is None: # list is empty
					self.tail = None
			else:
				previous.set_next(current.get_next())
				if current.get_next() is None: # Removing the tail
					self.tail = previous
		# decrease the count
		self.node_count -= 1

	def __str__(self):
		"""
        Return a string representation of the linked list in Python list format.

        Returns:
            str: A string representation of the linked list.
        """
		items = []
		current = self.head
		while current is not None:
			items.append(current.get_data())
			current = current.get_next()
		return str(items)

	def append(self,item):
		"""
		Append an item to the end of the linked list.
		@param item: Node
		"""
		temp = Node(item)
		if self.tail is None: #if list is empty
			self.head =temp
			self.tail = temp
		else:
			self.tail.set_next(temp)
			self.tail = temp
		self.node_count += 1

	def index(self,item):
		"""
		Returns the index of the first occurrence of an item in the list.
		@param item: Node
		@return: int value - index of the first occurrence of an item in the list.
		"""
		current = self.head #init a traversal through the list
		index = 0
		while current is not None:
			if current.get_data() == item:
				return index
			current = current.get_next()
			index += 1
		raise ValueError("Item not found")

	def pop(self,position = None):
		"""
		Removes and returns the item at the specified position.
		If no position is given, it removes the last item.
		@param position: int value
		@return: Node
		"""
		if position is None:
			position = self.size() - 1
		if position < 0 or position >= self.size():
			raise ValueError("Index out of range")

		current = self.head
		previous = None
		index = 0
		while index < position:
			previous = current
			current = current.get_next()
			index += 1

		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

		if current.get_next() is None: #If it was the last element, update tail
			self.tail = previous
		self.node_count -= 1
		return current.get_data() # Return the entire node

	def insert(self,position,item):
		"""
		Inserts an item at the specified position in the linked list.
		@param position:
		@param item:
		"""
		if position < 0 or position >= self.size():
			raise ValueError("Index out of range")
		temp = Node(item)
		current = self.head
		previous = None
		index = 0
		while index < position:
			previous = current
			current = current.get_next()
			index += 1

		if previous is None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current)
			previous.set_next(temp)

		if temp.get_next() is None: # Update tail if it added at the end
			self.tail = temp

		self.node_count += 1

	def reverse(self):
		"""
		Reverses the linked list in place. In-place.
		"""
		previous = None
		current = self.head
		self.tail = self.head # update the tail to be the current head
		while current is not None:
			next_node = current.get_next() # save the node
			current.set_next(previous) # Reverse the link
			previous = current # Move previous forward
			current = next_node # Move the current forward
		self.head = previous

	def slicing(self, start, stop):
		"""
		Returns a new list containing the items from start to stop indices. Don't count the item in stop position. (like a list)
		@param start:
		@param stop:
		@return:
		"""
		if start < 0 or stop > self.size() or start >= stop:
			raise ValueError("Invalid slice range")

		new_list = UnorderedList()
		current = self.head
		index = 0
		while current is not None and index < stop:
			if index >= start:
				new_list.append(current.get_data())
			current = current.get_next()
			index += 1

		return new_list

	def __iter__(self):
		"""Returns an iterator for the linked list."""
		current = self.head
		while current is not None:
			yield current.get_data()
			current = current.get_next()

if __name__ == "__main__":
	unordered_list = UnorderedList()
	unordered_list.add(10)
	unordered_list.add(20)
	unordered_list.add(30)
	unordered_list.add(20)  # Adding a duplicate
	unordered_list.append(123)
	print(unordered_list)  # Output: [20, 30, 20, 10]
	print(unordered_list.slicing(2,unordered_list.size()))
	unordered_list.reverse()
	print(unordered_list)
	print(20 in unordered_list)