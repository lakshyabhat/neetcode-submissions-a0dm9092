# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cNode = head
        while cNode:
            l += 1
            cNode = cNode.next
        curr = head
        c = l - n
        counter = -1
        p = ListNode()
        p.next = head
        res = p
        while counter!= c:
            counter += 1
            if counter == c:
                temp = p.next.next
                p.next = None
                p.next = temp
            p = p.next
        return res.next
            
            



        
