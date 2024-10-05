from node import Node


class OrderedList:
    """
    A class used to represent an OrderedList (Linked List).

    Attributes:
    -----------
    head : Node
        The head (first element) of the linked list.
    tail : Node
        The tail (last element) of the linked list.
    node_count : int
        The number of nodes in the linked list.

    Methods:
    --------
    search(item):
        Searches for an item in the linked list.
    add(item):
        Add an item to the linked list in the correct order.
    size():
        Returns the current size of the linked list.
    remove(item):
        Remove an item from the linked list.
    is_empty():
        Returns whether the linked list is empty.
    size():
        Returns the size of the linked list.
    index(item):
        Returns the index of the item in the linked list.
    pop(position):
		Removes and returns the item at the specified position.
		If no position is given, it removes the last item.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
        self.tail = None
        self.node_count = 0

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def size(self):
        """Returns the size of the linked list."""
        return self.node_count

    def search(self, item):
        """
        Search for an item in the linked list.

        Parameters:
            item : Any
                The value to search for in the linked list
        """
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        """
        Add an item to the linked list while maintaining order.
        Parameters:
            item : Any
                The value to add to the linked list.
        """
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)

        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        if temp.get_next() is None:
            self.tail = temp
        self.node_count += 1

    def remove(self, item):
        """
        Remove an item from the linked list.
        Parameters:
            item : Any
                The value to be removed from the linked list.
        """
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            raise ValueError("Item not found in the list.")

        if previous is None:
            # Remove head
            self.head = current.get_next()
            if self.head is None:
                # The List is now empty
                self.tail = None
        else:
            previous.set_next(current.get_next())
            if previous.get_next() is None:
                # If the removed item was the tail, update the tail
                self.tail = previous

        self.node_count -= 1

    def pop(self,position=None):
        """Remove and returns the item at the specified position.
		If no position is given, it removes the last item.
		@param position: int value
		@return: Node
		"""
        if position is None:
            position = self.size() - 1
        if position < 0 or position >= self.size():
            raise ValueError("Index out of range.")

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
        return current.get_data()

    def index(self, item):
        """
        Returns the index of the item in the linked list.
        @param item: Any
        """
        current = self.head  # init a traversal through the list
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError("Item not found")

    def __str__(self):
        """Returns a string representation of the linked list in Python list format."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return str(result)

    def __iter__(self):
        """Returns an iterator for the linked list."""
        current = self.head
        while current is not None:
            yield current.get_data()
            current = current.get_next()

    def append(self, item):
        """Adds an item to the linked list while maintaining the order."""
        self.add(item)

    def reverse(self):
        """
        Reverses the linked list in place. In-place.
        """
        previous = None
        current = self.head
        self.tail = self.head  # update the tail to be the current head
        while current is not None:
            next_node = current.get_next()  # save the node
            current.set_next(previous)  # Reverse the link
            previous = current  # Move previous forward
            current = next_node  # Move the current forward
        self.head = previous

if __name__ == "__main__":
    # Initialize an empty ordered list
    ol = OrderedList()

    # Add elements to the ordered list
    ol.add(5)
    ol.add(3)
    ol.add(10)
    ol.add(1)

    # Print the list after adding elements
    print("List after adding elements (should be ordered):")
    print(ol)  # Expected output: [1, 3, 5, 10]

    # Check the size of the list
    print("\nSize of the list:")
    print(ol.size())  # Expected output: 4

    # Search for an element in the list
    print("\nSearch for element 5:")
    print(ol.search(5))  # Expected output: True

    print("Search for element 7:")
    print(ol.search(7))  # Expected output: False

    # Remove an element from the list
    print("\nRemoving element 3:")
    ol.remove(3)
    print(ol)  # Expected output: [1, 5, 10]

    # Pop an element from the list
    print("\nPopping last element:")
    popped = ol.pop()
    print("Popped element:", popped)  # Expected output: 10
    print("List after popping:")
    print(ol)  # Expected output: [1, 5]

    # Pop an element from a specific position
    print("\nPopping element at position 0:")
    popped = ol.pop(0)
    print("Popped element:", popped)  # Expected output: 1
    print("List after popping:")
    print(ol)  # Expected output: [5]

    # Adding new elements to test add after pops
    ol.add(8)
    ol.add(4)
    print("\nList after adding elements 8 and 4:")
    print(ol)  # Expected output: [4, 5, 8]

    # Test index of an item
    print("\nIndex of element 5:")
    print(ol.index(5))  # Expected output: 1

    # Test appending an element
    print("\nAppending element 12:")
    ol.append(12)
    print(ol)  # Expected output: [4, 5, 8, 12]
