class Stack:
    """
    A class used to represent a Stack (LIFO - Last In First Out)

    Attributes:
    ----------
    items : list
    List to store stack elements

    Methods:
    -------
    is_empty():
        Checks if the stack is empty.
    push(item):
        Pushes an item onto the stack.
    pop():
        Pops the top item from the stack.
    peek():
        Returns the top item of the stack without removing it.
    size():
        Returns the current size of the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return self.items == []

    def push(self, item):
        """
        Add an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the item from the top of the stack.
        """
        return self.items.pop()

    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        """
        return self.items[-1] if not self.is_empty() else None  # Added safety for empty stack

    def size(self):
        """
        Get the number of items in the stack.
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        return str(self.items)

