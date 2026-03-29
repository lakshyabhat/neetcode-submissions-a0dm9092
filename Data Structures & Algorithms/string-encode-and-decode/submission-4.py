class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = ':'
        e = ''
        for word in strs:
            e = e + str(len(word)) + sep + word
        return e

    def decode(self, s: str) -> List[str]:
        res = []
        sep = ':'
        i = 0
        while i<len(s):
            k = i+1
            while s[k] !=  sep:
                k += 1
            l = int(s[i:k])
            res.append(s[k+1:k+l+1])
            i = k+l+1
        return res
