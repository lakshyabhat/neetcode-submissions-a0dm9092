class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j +=1 
            count = int(s[i:j])
            i = j+1
            j = i + count
            res.append(s[i:j])
            i = j
        return res