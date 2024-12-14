# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ADT_abstract_data_type.stack import Stack
# inorder traversal means left first - then root - then right
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    stack = Stack()
    cur = root
    result = []
    while cur or not stack.is_empty():
        if cur:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(current.value)
            cur = cur.right
    return result

