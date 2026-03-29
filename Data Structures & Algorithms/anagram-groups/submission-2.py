class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_d = {}
        for s in strs:
            c = [0]*26
            for l in s:
                c[ord('a') - ord(l)] += 1
            if tuple(c) not in ana_d:
                ana_d[tuple(c)] = [s]
            else:
                ana_d[tuple(c)].append(s)
        return list(ana_d.values())
