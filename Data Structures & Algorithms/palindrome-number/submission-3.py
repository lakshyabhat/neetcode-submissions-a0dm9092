class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        q = x
        while q>0:
           rev = rev*10 +q%10
           q = q//10
           
        return rev == x


