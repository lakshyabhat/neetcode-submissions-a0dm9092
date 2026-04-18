class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        minHeap = []
        res = []
        for key,v in c.items():
            heapq.heappush(minHeap,(v,key))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        for count,nums in minHeap:
            res.append(nums)
        
        return res
            