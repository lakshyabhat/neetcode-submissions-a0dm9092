class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = ''
        for l in s:
            if l.isalnum():
                processed_s += l.lower()
        return processed_s[::-1] == processed_s