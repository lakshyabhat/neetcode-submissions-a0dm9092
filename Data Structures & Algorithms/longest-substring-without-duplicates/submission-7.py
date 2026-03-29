class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        maxlong = 1
        if s == '':
            return 0
        while r<len(s):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                r += 1
                maxlong = max(maxlong,r-l)
            else:
                l +=1
                r = l+1
        return maxlong
            
