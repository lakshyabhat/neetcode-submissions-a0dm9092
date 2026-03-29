class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        place = 0
        rev = 0
        q = x
        while q>0:
           r = q%10
           q = q//10
           rev = r*(10**place) + rev*(10**(place+1))
        return rev == x


