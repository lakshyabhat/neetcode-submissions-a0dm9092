class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        i = 0
        is_pos = True
        if x<0:
            is_pos = False
            x = abs(x)
        while x>0:
            rev = rev*10 + x%10
            x = x//10
            i += 1
        if not is_pos:
            rev = -rev
        if -2**31<=rev<= (2**31 - 1):
            return rev
        return 0