class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for l in s:
            if l not in s_d:
                s_d[l] = 1
            else:
                s_d[l] += 1
        for l in t:
            if l not in t_d:
                t_d[l] = 1
            else:
                t_d[l] += 1
        return s_d == t_d