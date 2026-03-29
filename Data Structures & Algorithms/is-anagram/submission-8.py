class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_d[s[i]] = 1 + s_d.get(s[i],0)
            t_d[t[i]] = 1 + t_d.get(t[i],0)
        return s_d == t_d