class QueueWithTwoStacks:
    """
    A queue implementation using two stacks to achieve
    O(1) average time complexity for both enqueue and dequeue operations.

    This class simulates a FIFO (First In, First Out) queue by using two stacks:
    stack_a for enqueue operations and stack_b for dequeue operations.
    """

    def __init__(self):
        """Initialize two empty stacks for the queue."""
        self.stack_a = []  # Stack for enqueue operations
        self.stack_b = []  # Stack for dequeue operations

    def enqueue(self, value):
        """
        Add an element to the back of the queue.

        Parameters:
        ----------
        value : Any
            The element to be added to the queue.
        """
        self.stack_a.append(value)

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns:
        -------
        Any
            The element at the front of the queue.

        Raises:
        -------
        IndexError
            If the queue is empty when attempting to dequeue.
        """
        if not self.stack_b:  # If stack B is empty
            while self.stack_a:  # Move elements from stack A to stack B
                self.stack_b.append(self.stack_a.pop())
        if not self.stack_b:  # Check again if stack B is empty
            raise IndexError("Queue is empty")
        return self.stack_b.pop()

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return len(self.stack_a) == 0 and len(self.stack_b) == 0

    def size(self):
        """
        Return the size of the queue.

        Returns:
        -------
        int
            The total number of elements in the queue.
        """
        return len(self.stack_a) + len(self.stack_b)
