class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation that stores key-value pairs.
    Keys must be unique and comparable, and values can be any object.

    Attributes:
        root: The root node of the tree.
        size: The number of nodes in the tree.
    """

    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root = None
        self.size = 0

    def __len__(self):
        """Returns the number of nodes in the tree."""
        return self.size

    def length(self):
        """Returns the number of nodes in the tree (alias for __len__)."""
        return self.size

    def __iter__(self):
        """Iterator to traverse the tree (in-order traversal)."""
        return self.root.__iter__()

    def put(self, key, value):
        """
        Adds a key-value pair to the tree. If the key already exists, its value is updated.

        Args:
            key: The key for the node.
            value: The value to associate with the key.
        """
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current_node):
        """
        Recursive helper method to insert a key-value pair at the correct position.

        Args:
            key: The key for the node.
            value: The value to associate with the key.
            current_node: The current node being evaluated.
        """
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        """Allows setting key-value pairs using the assignment syntax (e.g., tree[key] = value)."""
        self.put(key, value)

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """
        Recursive helper method to find the node with the given key.

        Args:
            key: The key to search for.
            current_node: The current node being evaluated.

        Returns:
            The node with the matching key, or None if not found.
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """Allows retrieval of values using the indexing syntax (e.g., value = tree[key])."""
        return self.get(key)

    def __contains__(self, key):
        """Checks if a key exists in the tree."""
        return self._get(key, self.root) is not None

    def delete(self, key):
        """
        Removes the node with the given key from the tree.

        Args:
            key: The key of the node to remove.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.root.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        """Allows deletion of a node using the del syntax (e.g., del tree[key])."""
        self.delete(key)


class TreeNode:
    """
    Node class for the binary search tree, representing a single node with a key, value, and links to children.

    Attributes:
        key: The key for the node.
        payload: The value associated with the key.
        left_child: Left child node.
        right_child: Right child node.
        parent: Parent node.
    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        """Initializes a TreeNode with a key, value, optional children, and a parent."""
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        """Returns True if the node has a left child."""
        return self.left_child

    def has_right_child(self):
        """Returns True if the node has a right child."""
        return self.right_child

    def is_left_child(self):
        """Returns True if the node is a left child of its parent."""
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        """Returns True if the node is a right child of its parent."""
        return self.parent and self.parent.right_child == self

    def is_root(self):
        """Returns True if the node is the root node (has no parent)."""
        return not self.parent

    def is_leaf(self):
        """Returns True if the node has no children."""
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        """Returns True if the node has at least one child."""
        return self.right_child or self.left_child

    def has_both_children(self):
        """Returns True if the node has both a left and right child."""
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        """
        Replaces the node's data with a new key, value, and children.

        Args:
            key: The new key.
            value: The new value.
            lc: The new left child.
            rc: The new right child.
        """
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree[3] = "red"
    my_tree[4] = "blue"
    my_tree[6] = "yellow"
    my_tree[2] = "at"
    print(my_tree[6])  # Output: yellow
    print(my_tree[2])  # Output: at
