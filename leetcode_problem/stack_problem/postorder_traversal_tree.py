# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ADT_abstract_data_type.stack import Stack
# postorder traversal means  left - right - root
# Using two stacks:
# stack1: push the root, while stack1 is not empty, it pops a node, pushed it onto stack2 (reversing the order), and
#         push its left and right children (if they exist)
# stack2: the elements in stack2 are now in reverse postorder. Pop them to get the correct one.
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack1 = Stack()
    stack2 = Stack()
    result = []
    stack1.push(root)
    while not stack1.is_empty():
        node = stack1.pop()
        stack2.push(node)
        if node.left:
            stack1.push(node.left)
        if node.right:
            stack1.push(node.right)

    while not stack2.is_empty():
        result.append(stack2.pop().val)
    return result




