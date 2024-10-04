class Node:
    """
    A class used to represent a Node in a linked list.

    Attributes:
    ----------
    data : Any
        The data to be stored in the node.
    next : Node
        A reference to the next node in the linked list.

    Methods:
    -------
    get_data():
        Returns the data stored in the node.
    get_next():
        Returns the reference to the next node.
    set_data(new_data):
        Sets the data stored in the node.
    set_next(new_next):
        Sets the reference to the next node.
    """

    def __init__(self, init_data):
        """
        Initialize a node with data.

        Parameters:
            init_data: The data to be stored in the node.
        """
        self.data = init_data
        self.next = None

    def get_data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.data

    def get_next(self):
        """
        Get the reference to the next node in the linked list.

        Returns:
            Node: The reference to the next node.
        """
        return self.next

    def set_data(self, new_data):
        """
        Set the data stored in the node.

        Parameters:
            new_data: The new data to be stored in the node.
        """
        self.data = new_data

    def set_next(self, new_next):
        """
        Set the reference to the next node.

        Parameters:
            new_next: The new reference to the next node.
        """
        self.next = new_next
