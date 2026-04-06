class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <2:
            return stones[0]
        maxHeap = []
        
        for stone in stones:
            heapq.heappush(maxHeap,-stone)
        while len(maxHeap)>1:    
            heavy = -heapq.heappop(maxHeap)
            light = -heapq.heappop(maxHeap)
            if heavy > light:
                newStone = heavy - light
                heapq.heappush(maxHeap,-newStone)

        return -maxHeap[0] if maxHeap else 0
        