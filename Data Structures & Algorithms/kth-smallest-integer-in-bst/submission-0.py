# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def trav(root, elem=[]):
            if root.left:
                trav(root.left,elem)
            if not root.left and not root.right:
                elem.append(root.val)
                return elem
            elem.append(root.val)
            if root.right:
                trav(root.right,elem)
            return elem
        return trav(root)[k-1]
            
