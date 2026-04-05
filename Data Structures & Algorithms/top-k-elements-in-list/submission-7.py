class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []
        for key,c in count.items():
            heapq.heappush(heap,(c,key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [num for key,num in heap]
        return res