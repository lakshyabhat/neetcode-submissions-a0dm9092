class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).items()
        res = []
        print(c)
        sorted_c = sorted(c,key = lambda x:x[1],reverse=True)[:k]
        for k,v in sorted_c:
            res.append(k)
        return res