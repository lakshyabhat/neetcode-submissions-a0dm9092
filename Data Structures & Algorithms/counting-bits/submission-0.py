class Solution:
    def countBits(self, n: int) -> List[int]:
        c = []
        for i in range(n+1):
            s = 0
            for l in list(bin(i).replace("0b","")):
                s += int(l)
            c.append(s)
        return c