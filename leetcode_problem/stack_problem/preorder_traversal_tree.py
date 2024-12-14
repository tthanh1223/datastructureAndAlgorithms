# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ADT_abstract_data_type.stack import Stack
# inorder traversal means root - then left - then right
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack = Stack()
    stack.push(root)
    result = []
    while not stack.is_empty():
        cur = stack.pop()
        result.append(cur.val)
        if cur.right:
            stack.push(cur.right)
        if cur.left:
            stack.push(cur.left)
    return result
