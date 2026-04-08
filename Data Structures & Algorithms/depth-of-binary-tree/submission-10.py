# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], length = 0) -> int:
        if not root:
            return length
        
        res = max(self.maxDepth(root.left,length+1),self.maxDepth(root.right,length+1))

        return res