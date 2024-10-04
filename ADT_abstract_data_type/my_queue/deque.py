class Deque:
    """
    A double-ended queue (deque) data structure that allows insertion and removal
    from both the front and the rear ends.

    Attributes:
    -----------
    items : list
        An Internal list used to store deque elements.

    Methods:
    --------
    is_empty() → bool
        Returns True if the deque is empty, otherwise False.

    Add_rear(value)
        Adds an element to the rear of the deque.

    Add_front(value)
        Adds an element to the front of the deque.

    Remove_rear() → Any
        Removes and returns the element from the rear of the deque.

    Remove_front() → Any
        Removes and returns the element from the front of the deque.

    Size() → int
        Returns the number of elements in the deque.

    __str__() → str
        Returns a string representation of the deque.
    """

    def __init__(self):
        """Initializes an empty deque."""
        self.items = []

    def is_empty(self):
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, otherwise False.
        """
        return self.items == []

    def add_rear(self, value):
        """
        Adds an element to the rear of the deque.

        Args:
            value: The value to be added to the rear.
        """
        self.items.insert(0, value)

    def add_front(self, value):
        """
        Adds an element to the front of the deque.

        Args:
            value: The value to be added to the front.
        """
        self.items.append(value)

    def remove_rear(self):
        """
        Removes and returns the element from the rear of the deque.

        Returns:
            The value removed from the rear of the deque.
        """
        return self.items.pop()

    def remove_front(self):
        """
        Removes and returns the element from the front of the deque.

        Returns:
            The value removed from the front of the deque.
        """
        return self.items.pop(0)

    def size(self):
        """
        Returns the number of elements in the deque.

        Returns:
            int: The size of the deque.
        """
        return len(self.items)

    def __str__(self):
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the elements of the deque.
        """
        return str(self.items)



