# create AVL Node
class AVLNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1

    def left_height(self):
        """
        Get the height of the left subtree
        @return: int
            height of the left subtree
        """
        return 0 if self.left is None else self.left.height

    def right_height(self):
        """
        Get the height of the right subtree
        @return: int
            height of the right subtree
        """
        return 0 if self.right is None else self.right.height

    def balance_factor(self):
        """
        Get the balance factor of the node
        @return: int
        """
        return self.left_height() - self.right_height()

    def update_height(self):
        """
        Update the height of the node
        @return: none
        """
        self.height = 1 + max(self.left_height(), self.right_height())

    def set_left(self, node):
        """
        Set the left child of the node
        @param node: AVLNode
        @return: none
        """
        self.left = node
        if node is not None:
            node.parent = self
        self.update_height()

    def set_right(self, node):
        """
        Set the right child of the node
        @param node: AVLNode
        @return: none
        """
        self.right = node
        if node is not None:
            node.parent = self
        self.update_height()

    def is_left_child(self):
        """
        Check whether this node is a left child
        @return: bool
        """
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        """
        Check whether this node is a right child
        @return: bool
        """
        return self.parent is not None and self.parent.right == self

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    @staticmethod
    def rotate_left(a: AVLNode):
        """
        Left rotation on node a
        @param a: AVLNode
        @return: b: AVLNode
            node which is left rotated by a
        """
        b = a.right
        # The new right child of A becomes the left child of B
        a.set_right(b.left)
        # The new left child of B becomes A
        b.set_left(a)
        return b # Return B to replace A with it

    @staticmethod
    def rotate_right(a: AVLNode):
        """
        Right rotation on node a
        @param a: AVLNode
        @return: b: AVLNode
            node which a right rotates
        """
        b = a.left
        a.set_left(b.right)
        b.set_right(a)
        return b

    def rebalance(self, node):
        if node is None:
            #Empty tree, no balancing needed
            return None
        balance = node.balance_factor()
        if abs(balance) <= 1:
            # The node is already balanced, no balancing needed
            return node
        if balance == 2:
            # Cases 1 and 2, the tree is leaning to the left
            if node.left.balance_factor() == -1:
                # Case 2, we first do a left rotation
                node.set_left(self.rotate_left(node.left))
            return self.rotate_right(node)
        # Balance must be -2
        # Case 3 and 4: the tree is leaning to the left
        if node.right.balance_factor() == -1:
            # Case 4, we first do a right rotation
            node.set_right(self.rotate_right(node.right))
        return self.rotate_left(node)



    def add(self, value):
        self.size += 1
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if value < current.value:
                # Value to insert is smaller than node value, go left
                current = current.left
            else:
                # Value to insert is larger than node value, go right
                current = current.right
        # We found the parent, create the new node
        new_node = AVLNode(value, parent)
        # Case 1: The parent is `None` so the new node is the root
        if parent is None:
            self.root = new_node
        else:
            # Case 2: Set the new node as a child of the parent
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
        # After a new node is added, we need to restore balance
        self.restore_balance(new_node)

    def restore_balance(self, node):
        current = node
        # Go up the tree and rebalance left and right children
        while current is not None:
            current.set_left(self.rebalance(current.left))
            current.set_right(self.rebalance(current.right))
            current.update_height()
            current = current.parent
        self.root = self.rebalance(self.root)
        self.root.parent = None

    def leftmost(self, starting_node):
        # Find the leftmost node from a given starting node
        previous = None
        current = starting_node
        while current is not None:
            previous = current
            current = current.left
        return previous

    def minimum(self):
        # Return the minimum value in the tree
        if self.root is None:
            raise Exception("Empty tree")
        return self.leftmost(self.root).value

    def rightmost(self, starting_node):
        # Find the rightmost node from a given starting node
        previous = None
        current = starting_node
        while current is not None:
            previous = current
            current = current.right
        return previous

    def maximum(self):
        # Find the maximum value in the tree
        if self.root is None:
            raise Exception("Empty tree")
        return self.rightmost(self.root).value

    def locate_node(self,value):
        """
        Return the node containing a given value None if no
        @param value: Any
        @return: bool
        """
        # such node exists
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
        node = self.locate_node(item)
        return node is not None

    def delete_leaf(self,node):
        if node.parent is None:
            self.root = None
        elif node.is_left_child():
            node.parent.left = None
            node.parent = None
        else:
            node.parent.right = None
            node.parent = None

    def delete(self,value):
        # Check if the node exists
        node = self.locate_node(value)
        if node is None:
            raise Exception("Value not found in tree")
        replacement = None
        rebalance_node = node.parent
        if node.left is not None:
            #There's a left child so we replace it with rightmost node
            replacement = self.rightmost(node.left)
            #Check if reparenting is necessary
            if replacement.is_left_child():
                replacement.parent.set_left(replacement.left)
            else:
                replacement.parent.set_right(replacement.right)
        if replacement:
            #We found a replacement so replace the value
            node.value = replacement.value
            rebalance_node = replacement.parent
        else:
            #No replacement, so it means the node to delete is a leaf
            self.delete_leaf(node)
        if rebalance_node is not None:
            self.restore_balance(rebalance_node)

    def search(self, node, lb, ub, results):
        #Search for values between lower bound and upper bound
        if node is None:
            return
        if lb <= node.value <= ub:
            results.append(node.value)
        if node.value >= lb:
            self.search(node.left, lb, ub, results)
        if node.value <= ub:
            self.search(node.right, lb, ub, results)

    def range_query(self, lb, ub):
        # Search for values between lower bound and upper bound
        results = []
        self.search(self.root, lb, ub, results)
        return results

