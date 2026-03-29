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
        
        for k,v in d_s.items():
            if k in d_t:
                if v != d_t[k]:
                    return False
            else:
                return False 
        
        for k,v in d_t.items():
            if k in d_s:
                if v != d_s[k]:
                    return False
            else:
                return False 

        return d_t == d_s
