class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        res = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in group:
                group[sorted_s] = [s]
            else:
                group[sorted_s].append(s)
        for k,v in group.items():
            res.append(v)
        return res