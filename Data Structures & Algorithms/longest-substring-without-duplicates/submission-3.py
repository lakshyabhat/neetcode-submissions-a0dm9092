class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l, r = 0, 1
        if l>len(s)-1:
            return 0
        sub.add(s[l])
        res = 1
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                res = max(res,r-l+1)
                r += 1
            else:
                sub.clear()
                l += 1
                if l<len(s):
                    sub.add(s[l])
                r = l+1
        return res
            
