class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s, d_t = {}, {}
        for l in s:
            if l not in d_s:
                d_s[l] = 1
            else:
                d_s[l] += 1
        
        for l in t:
            if l not in d_t:
                d_t[l] = 1
            else:
                d_t[l] += 1

        return d_t == d_s
