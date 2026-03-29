class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = defaultdict(int),defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_d[s[i]] += 1
            t_d[t[i]] += 1
        return s_d == t_d