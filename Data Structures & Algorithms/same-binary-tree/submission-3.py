# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])
        while queue_p and queue_q:
            for i in range(len(queue_p)):
                curr_p = queue_p.popleft()
                curr_q = queue_q.popleft()
                
                if curr_p is None and curr_q is None:
                    continue

                if curr_p is None or curr_q is None or curr_p.val != curr_q.val:
                    return False
                
                queue_p.append(curr_p.left)
                queue_q.append(curr_q.left)            
                queue_p.append(curr_p.right)
                queue_q.append(curr_q.right)
                
        return not queue_p and not queue_q

                

                
                   




                