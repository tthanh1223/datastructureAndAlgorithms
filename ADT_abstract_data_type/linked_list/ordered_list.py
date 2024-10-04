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
        Adds an item to the linked list in the correct order.
    size():
        Returns the current size of the linked list.
    remove(item):
        Removes an item from the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
        self.tail = None
        self.node_count = 0

    def search(self, item):
        """
        Search for an item in the linked list.

        Parameters:
            item : Any
                The value to search for in the linked list.

        Returns:
            bool: True if the item is found, False otherwise.
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

    def size(self):
        """
        Get the number of items in the linked list.

        Returns:
            int: The number of items in the linked list.
        """
        return self.node_count

    def remove(self, item):
        """
        Remove an item from the linked list.

        Parameters:
            item : Any
                The value to be removed from the linked list.

        Raises:
            ValueError: If the item is not found in the linked list.
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
                # List is now empty
                self.tail = None
        else:
            previous.set_next(current.get_next())
            if previous.get_next() is None:
                # If the removed item was the tail, update the tail
                self.tail = previous

        self.node_count -= 1
