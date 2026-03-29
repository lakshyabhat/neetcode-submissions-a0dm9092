class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for i in range(len(nums)+1)]
        res = []

        c = Counter(nums)
        for n,count in c.items():
            l[count].append(n)
        

        for i in range(len(l)-1,-1,-1):
            for freq in l[i]:
                res.append(freq)
                if len(res) == k:
                    return res
        
        return