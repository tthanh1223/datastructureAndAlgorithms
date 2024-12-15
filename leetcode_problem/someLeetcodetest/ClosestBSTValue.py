class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def insert_left(self, value):
        """Inserts a new TreeNode with the given value to the left of the current node."""
        self.left = TreeNode(value)

    def insert_right(self, value):
        """Inserts a new TreeNode with the given value to the right of the current node."""
        self.right = TreeNode(value)

    def is_leaf(self):
        """Checks if the current node is a leaf (i.e., it has no children)."""
        return self.left is None and self.right is None

    def __repr__(self):
        """Provides a string representation of the tree rooted at this node."""
        def recurse(node):
            if node is None:
                return "None"
            left = recurse(node.left)
            right = recurse(node.right)
            return f"TreeNode(val={node.val}, left={left}, right={right})"
        return recurse(self)


def closestValue(root: TreeNode, target: float) -> int:
    closest = root.val
    while root is not None:
        if abs(root.val - target) < abs(target - closest): closest = root.val
        if root.val == target: return closest
        elif root.val > target :
            root = root.left
        else : root = root.right
    return closest
# Assume the following BST structure:
#         4
#        / \
#       2   5
#      / \
#     1   3
root = TreeNode(4)

# Insert left and right children
root.insert_left(2)
root.insert_right(5)

# Further insertions
root.left.insert_left(1)
root.left.insert_right(3)

# Check if a node is a leaf
print(root.left.is_leaf())  # Output: False (since it has children)

# Print the tree
print(root)  #
target = 3.7
result = closestValue(root, target)
print(result)  # Output: 4 (since 4 is the closest to 3.7)

target = 1
result = closestValue(root, target)
print(result)  # Output: 2 (since 2 is the closest to 2.5)