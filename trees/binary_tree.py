class BinaryTree:
    """
    Represent a binary tree structure.

    Attributes:
    -----------
    key : Any
        The value stored in the root node of the tree.
    left_child : BinaryTree or None
        The left child subtree, which is either another BinaryTree or None.
    right_child : BinaryTree or None
        The right child subtree, which is either another BinaryTree or None.
    """

    def __init__(self, root):
        """
        Initialize a BinaryTree with the root value.

        Parameters:
        -----------
        root : Any
            The value to store in the root of the tree.
        """
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        """
        Insert a new node as the left child of the tree. If there is already a left child,
        it moves down as the left child of the newly inserted node.

        Parameters:
        -----------
        node : Any
            The value to insert as the left child of the current node.
        """
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, node):
        """
        Insert a new node as the right child of the tree. If there is already a right child,
        it moves down as the right child of the newly inserted node.

        Parameters:
        -----------
        node : Any
            The value to insert as the right child of the current node.
        """
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        """
        Get the right child subtree.

        Returns:
        --------
        BinaryTree or None
            The right child subtree, or None if there is no right child.
        """
        return self.right_child

    def get_left_child(self):
        """
        Get the left child subtree.

        Returns:
        --------
        BinaryTree or None
            The left child subtree, or None if there is no left child.
        """
        return self.left_child

    def set_root_val(self, value):
        """
        Set the value of the root node.

        Parameters:
        -----------
        value : Any
            The new value for the root node.
        """
        self.key = value

    def get_root_val(self):
        """
        Get the value of the root node.

        Returns:
        --------
        Any
            The value stored in the root node.
        """
        return self.key

def preorder(a_tree: BinaryTree):
    """
     we visit the root node first,
     then recursively do a preorder traversal of the left subtree,
     followed by a recursive preorder traversal of the right subtree.
    """
    if a_tree:
        print(a_tree.get_root_val())
        preorder(a_tree.get_left_child())
        preorder(a_tree.get_right_child())

def inorder(a_tree: BinaryTree):
    if a_tree:
        inorder(a_tree.get_left_child())
        print(a_tree.get_root_val())
        inorder(a_tree.get_right_child())

def postorder(a_tree:BinaryTree):
    if a_tree:
        postorder(a_tree.get_left_child())
        postorder(a_tree.get_right_child())
        print(a_tree.get_root_val())


