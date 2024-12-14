# AVL Tree Implementation in Python with Comprehensive Documentation

class AVLNode:
    """
    Represents a node in an AVL Tree.
    Attributes:
        value (Any): The value stored in the node.
        parent (AVLNode, optional): Reference to the parent node. Defaults to None.
        left (AVLNode, optional): Reference to the left child. Defaults to None.
        right (AVLNode, optional): Reference to the right child. Defaults to None.
        height (int): The height of the node in the tree. Defaults to 1.
    """

    def __init__(self, value, parent=None):
        """
        Initializes an AVLNode with the given value and optional parent.

        Args:
            value (Any): The value to store in the node.
            parent (AVLNode, optional): The parent node. Defaults to None.
        """
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1

    def left_height(self):
        """
        Retrieves the height of the left subtree.

        Returns:
            int: Height of the left subtree. Returns 0 if there is no left child.
        """
        return 0 if self.left is None else self.left.height

    def right_height(self):
        """
        Retrieves the height of the right subtree.

        Returns:
            int: Height of the right subtree. Returns 0 if there is no right child.
        """
        return 0 if self.right is None else self.right.height

    def balance_factor(self):
        """
        Calculates the balance factor of the node.

        Balance Factor = Height of Left Subtree - Height of Right Subtree

        Returns:
            int: The balance factor of the node.
        """
        return self.left_height() - self.right_height()

    def update_height(self):
        """
        Updates the height of the node based on the heights of its children.

        The height is set to 1 plus the maximum height of its left or right subtree.
        """
        self.height = 1 + max(self.left_height(), self.right_height())

    def set_left(self, node):
        """
        Sets the left child of the node and updates parent references and height.

        Args:
            node (AVLNode): The node to set as the left child.
        """
        self.left = node
        if node is not None:
            node.parent = self
        self.update_height()

    def set_right(self, node):
        """
        Sets the right child of the node and updates parent references and height.

        Args:
            node (AVLNode): The node to set as the right child.
        """
        self.right = node
        if node is not None:
            node.parent = self
        self.update_height()

    def is_left_child(self):
        """
        Determines if the node is a left child of its parent.

        Returns:
            bool: True if the node is a left child, False otherwise.
        """
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        """
        Determines if the node is a right child of its parent.

        Returns:
            bool: True if the node is a right child, False otherwise.
        """
        return self.parent is not None and self.parent.right == self


class AVLTree:
    """
    Represents an AVL (Adelson-Velsky and Landis) Tree, a self-balancing binary search tree.

    Attributes:
        root (AVLNode, optional): The root node of the AVL tree. Defaults to None.
        size (int): The number of nodes in the AVL tree. Defaults to 0.
    """

    def __init__(self):
        """
        Initializes an empty AVLTree.
        """
        self.root = None
        self.size = 0

    @staticmethod
    def rotate_left(a: AVLNode):
        """
        Performs a left rotation on the given node 'a'.

        Left Rotation Diagram:
            a                 b
             \               / \
              b     =>      a   c
             / \             \
            t1  c             t1

        Args:
            a (AVLNode): The node to perform a left rotation on.

        Returns:
            AVLNode: The new root node after rotation.
        """
        b = a.right
        # The new right child of A becomes the left child of B
        a.set_right(b.left)
        # The new left child of B becomes A
        b.set_left(a)
        return b  # Return B to replace A with it

    @staticmethod
    def rotate_right(a: AVLNode):
        """
        Performs a right rotation on the given node 'a'.

        Right Rotation Diagram:
              a               b
             /               / \
            b       =>      c   a
           / \                 /
          c   t1              t1

        Args:
            a (AVLNode): The node to perform a right rotation on.

        Returns:
            AVLNode: The new root node after rotation.
        """
        b = a.left
        # The new left child of A becomes the right child of B
        a.set_left(b.right)
        # The new right child of B becomes A
        b.set_right(a)
        return b  # Return B to replace A with it

    def rebalance(self, node):
        """
        Rebalances the subtree rooted at the given node if it is unbalanced.

        Args:
            node (AVLNode): The node to rebalance.

        Returns:
            AVLNode: The new root of the rebalance subtree.
        """
        if node is None:
            # Empty subtree, no balancing needed
            return None

        balance = node.balance_factor()

        if abs(balance) <= 1:
            # The node is already balanced, no balancing needed
            return node

        if balance == 2:
            # The tree is left-heavy
            if node.left.balance_factor() == -1:
                # Left-Right Case: first rotate left on the left child
                node.set_left(self.rotate_left(node.left))
            # Left-Left Case: rotate right on the unbalanced node
            return self.rotate_right(node)

        if balance == -2:
            # The tree is right-heavy
            if node.right.balance_factor() == 1:
                # Right-Left Case: first rotate right on the right child
                node.set_right(self.rotate_right(node.right))
            # Right-Right Case: rotate left on the unbalanced node
            return self.rotate_left(node)

        # If balance factor is not 2 or -2, return node as is
        return node

    def add(self, value):
        """
        Inserts a new value into the AVL tree.

        Args:
            value (Any): The value to insert into the tree.
        """
        self.size += 1
        parent = None
        current = self.root

        # Traverse the tree to find the insertion point
        while current is not None:
            parent = current
            if value < current.value:
                # Value to insert is smaller than current node's value, go left
                current = current.left
            else:
                # Value to insert is greater or equal, go right
                current = current.right

        # Create the new node with the found parent
        new_node = AVLNode(value, parent)

        if parent is None:
            # Case 1: The tree was empty, new node becomes the root
            self.root = new_node
        else:
            # Case 2: Set the new node as a left or right child of the parent
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

        # After insertion, restore the AVL property by rebalancing
        self.restore_balance(new_node)

    def restore_balance(self, node):
        """
        Restores the AVL tree balance by traversing up from the given node
        and performing necessary rotations.

        Args:
            node (AVLNode): The node from which to start restoring balance.
        """
        current = node
        # Traverse up to the root, rebalancing along the path
        while current is not None:
            # Rebalance the left and right subtrees of the current node
            current.set_left(self.rebalance(current.left))
            current.set_right(self.rebalance(current.right))
            # Update the height of the current node after potential rotations
            current.update_height()
            # Move up to the parent node
            current = current.parent

        # Finally, rebalance the root in case rotations have affected it
        self.root = self.rebalance(self.root)
        if self.root:
            self.root.parent = None  # Ensure the root has no parent

    def leftmost(self, starting_node):
        """
        Finds the leftmost (minimum) node starting from the given node.

        Args:
            starting_node (AVLNode): The node from which to start the search.

        Returns:
            AVLNode: The leftmost node in the subtree.
        """
        previous = None
        current = starting_node
        while current is not None:
            previous = current
            current = current.left
        return previous

    def minimum(self):
        """
        Retrieves the minimum value stored in the AVL tree.

        Returns:
            Any: The smallest value in the tree.

        Raises:
            Exception: If the tree is empty.
        """
        if self.root is None:
            raise Exception("Empty tree")
        return self.leftmost(self.root).value

    def rightmost(self, starting_node):
        """
        Finds the rightmost (maximum) node starting from the given node.

        Args:
            starting_node (AVLNode): The node from which to start the search.

        Returns:
            AVLNode: The rightmost node in the subtree.
        """
        previous = None
        current = starting_node
        while current is not None:
            previous = current
            current = current.right
        return previous

    def maximum(self):
        """
        Retrieves the maximum value stored in the AVL tree.

        Returns:
            Any: The largest value in the tree.

        Raises:
            Exception: If the tree is empty.
        """
        if self.root is None:
            raise Exception("Empty tree")
        return self.rightmost(self.root).value

    def locate_node(self, value):
        """
        Searches for a node containing the given value.

        Args:
            value (Any): The value to search for.

        Returns:
            AVLNode or None: The node containing the value if found, else None.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def __contains__(self, item):
        """
        Enables the use of the 'in' keyword to check for value existence in the AVL tree.

        Args:
            item (Any): The value to check for.

        Returns:
            bool: True if the value exists in the tree, False otherwise.
        """
        node = self.locate_node(item)
        return node is not None

    def delete_leaf(self, node):
        """
        Deletes a leaf node from the AVL tree.

        Args:
            node (AVLNode): The leaf node to delete.
        """
        if node.parent is None:
            # The node is the root and the only node in the tree
            self.root = None
        elif node.is_left_child():
            # The node is a left child
            node.parent.left = None
            node.parent = None
        else:
            # The node is a right child
            node.parent.right = None
            node.parent = None

    def delete(self, value):
        """
        Deletes a node with the specified value from the AVL tree.

        Args:
            value (Any): The value to delete from the tree.

        Raises:
            Exception: If the tree is empty or the value is not found.
        """
        # Locate the node to delete
        node = self.locate_node(value)
        if node is None:
            raise Exception("Value not found in tree")
        replacement = None
        rebalance_node = node.parent

        if node.left is not None:
            # Node has a left child; find the rightmost node in the left subtree
            replacement = self.rightmost(node.left)
            # Reparenting if necessary
            if replacement.is_left_child():
                replacement.parent.set_left(replacement.left)
            else:
                replacement.parent.set_right(replacement.right)

        if replacement:
            # Replace node's value with replacement's value
            node.value = replacement.value
            rebalance_node = replacement.parent
        else:
            # Node is a leaf; delete it directly
            self.delete_leaf(node)

        if rebalance_node is not None:
            # Restore balance starting from the parent of the deleted node
            self.restore_balance(rebalance_node)
        self.size -= 1

    def search(self, node, lb, ub, results):
        """
        Recursively searches for values within a given range and appends them to results.

        Args:
            node (AVLNode): The current node in the traversal.
            lb (Any): The lower bound of the range.
            ub (Any): The upper bound of the range.
            results (list): The list to append found values to.
        """
        if node is None:
            return
        if lb <= node.value <= ub:
            results.append(node.value)
        if node.value >= lb:
            self.search(node.left, lb, ub, results)
        if node.value <= ub:
            self.search(node.right, lb, ub, results)

    def range_query(self, lb, ub):
        """
        Searches for and retrieves all values within the specified range [lb, ub].

        Args:
            lb (Any): The lower bound of the range.
            ub (Any): The upper bound of the range.

        Returns:
            list: A list of values within the specified range.
        """
        results = []
        self.search(self.root, lb, ub, results)
        return results

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the AVL tree.

        Returns:
            list: A list of values in in-order sequence.
        """
        elements = []
        self._inorder_helper(self.root, elements)
        return elements

    def _inorder_helper(self, node, elements):
        """
        Helper method for in-order traversal.

        Args:
            node (AVLNode): The current node in traversal.
            elements (list): The list accumulating traversal results.
        """
        if node:
            self._inorder_helper(node.left, elements)
            elements.append(node.value)
            self._inorder_helper(node.right, elements)

    def preorder_traversal(self):
        """
        Performs a pre-order traversal of the AVL tree.

        Returns:
            list: A list of values in pre-order sequence.
        """
        elements = []
        self._preorder_helper(self.root, elements)
        return elements

    def _preorder_helper(self, node, elements):
        """
        Helper method for pre-order traversal.

        Args:
            node (AVLNode): The current node in traversal.
            elements (list): The list accumulating traversal results.
        """
        if node:
            elements.append(node.value)
            self._preorder_helper(node.left, elements)
            self._preorder_helper(node.right, elements)

    def postorder_traversal(self):
        """
        Performs a post-order traversal of the AVL tree.

        Returns:
            list: A list of values in post-order sequence.
        """
        elements = []
        self._postorder_helper(self.root, elements)
        return elements

    def _postorder_helper(self, node, elements):
        """
        Helper method for post-order traversal.

        Args:
            node (AVLNode): The current node in traversal.
            elements (list): The list accumulating traversal results.
        """
        if node:
            self._postorder_helper(node.left, elements)
            self._postorder_helper(node.right, elements)
            elements.append(node.value)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        """
        Prints a visual representation of the AVL tree.

        Args:
            node (AVLNode, optional): The current node to print. Defaults to None, which starts with the root.
            level (int, optional): The current depth level in the tree. Defaults to 0.
            prefix (str, optional): The prefix string to indicate the branch type. Defaults to "Root: ".
        """
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

    def __len__(self):
        """
        Returns the number of nodes in the AVL tree.

        Returns:
            int: The size of the tree.
        """
        return self.size

    def is_balanced(self):
        """
        Checks if the AVL tree is balanced according to AVL properties.

        Returns:
            bool: True if the tree is balanced, False otherwise.
        """

        def check_balance(node):
            if node is None:
                return True
            balance = node.balance_factor()
            if abs(balance) > 1:
                return False
            return check_balance(node.left) and check_balance(node.right)

        return check_balance(self.root)

    def __iter__(self):
        pass
