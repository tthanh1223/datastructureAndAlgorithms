class CustomQueue:
    """
    a simple implementation of a queue data structure using Python lists,
    where elements are inserted at the front and removed from the end.
    this maintains the FIFO (First In - First Out) principle.

    methods:
    --------
    enqueue(value): Add an element to the back of the queue.
    dequeue(): Remove and return the front element of the queue.
    size(): Return the size of the queue.
    is_empty(): Check if the queue is empty.
    __str__(): Return a string representation of the queue.
    """
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []  # List to store queue elements
        self.front = 0  # Pointer to the tail of the queue

    def enqueue(self, value):
        """
        Adds an element to the back of the queue.

        Parameters:
        ----------
        value: Any
            The element to be added to the queue.
        """
        self.items.insert(0, value)  # Insert at the front
        self.front += 1  # Increment the size

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Returns:
        -------
        Any
            The element at the front of the queue.

        Raises:
        -------
        IndexError
            If the queue is empty when attempting to dequeue.
        """
        if self.is_empty():
            raise IndexError('Queue is empty')
        self.front -= 1  # Decrement the size
        return self.items.pop()  # Remove and return the last element

    def size(self):
        """
        Returns the size of the queue.

        Returns:
        -------
        int
            The size of the queue.
        """
        return self.front

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return self.front == 0

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
        -------
        str
            A string showing the elements in the queue.
        """
        return str(self.items)
