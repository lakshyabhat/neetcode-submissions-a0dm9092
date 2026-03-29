class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <right:
            if s[left].isalnum()!=True:
                left +=1
                continue
            if s[right].isalnum()!=True:
                right -=1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True 
            