# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        res = curr
        carry = 0
        while l1 is not None or l2 is not None:
            if l2 is None:
                total = l1.val + carry
            elif l1 is None:
                total = l2.val + carry
            else:
                total = l1.val + l2.val + carry
            if len(str(total))>1:
                carry = int(str(total)[0])
                unit = int(str(total)[1])
            else:
                unit = total  
                carry = 0  
            curr.next = ListNode(unit)
            curr = curr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry != 0:
            curr.next = ListNode(carry)
        return res.next