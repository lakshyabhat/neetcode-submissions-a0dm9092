class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_w = ''
        for w in s:
            if w.isalnum():
                p_w = p_w + w.lower()
        left = 0
        right = len(p_w) - 1
        while right>=left:
            if p_w[left] != p_w[right]:
                return False
            left += 1
            right -= 1
        return True
