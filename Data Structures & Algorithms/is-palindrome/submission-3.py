class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ''
        for l in s:
            if l.isalnum():
                processed += l.lower()
        return processed == ''.join(list(processed)[::-1])