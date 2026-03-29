class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            c = [0]*26
            for l in s:
                i = ord(l) - ord('a')
                c[i] += 1
            res[tuple(c)].append(s)

        return list(res.values())