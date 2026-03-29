class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_w = ''
        word = ("".join(s.split())).lower()
        for w in word:
            if w.isalnum():
                p_w += w
        print(p_w[::-1])
        return p_w == p_w[::-1]