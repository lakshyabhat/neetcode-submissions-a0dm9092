class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = [0]*26
        t_count = [0]*26
        for i in range(len(s)):
            index_s = ord('a') - ord(s[i])
            index_t = ord('a') - ord(t[i])
            s_count[index_s] += 1
            t_count[index_t] += 1
        return s_count == t_count

