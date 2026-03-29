class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        values_sort = sorted(list(count.values()),reverse=True)[:k]

        for n,c in count.items():
            if c in set(values_sort):
                res.append(n)
        
        return res