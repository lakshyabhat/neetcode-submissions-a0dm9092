class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_d = {}
        for s in strs:
            if ''.join(sorted(s)) in ana_d:
                ana_d[''.join(sorted(s))].append(s)
            else:
                 ana_d[''.join(sorted(s))] = [s]
        return list(ana_d.values())