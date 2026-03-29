class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_d = defaultdict(list)
        for s in strs:
            c = [0]*26
            for l in s:
                c[ord('a') - ord(l)] += 1
            ana_d[tuple(c)].append(s)
        return list(ana_d.values())
