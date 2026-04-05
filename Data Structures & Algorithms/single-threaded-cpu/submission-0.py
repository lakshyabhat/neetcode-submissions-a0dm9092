class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,task in enumerate(tasks):
            task.append(i)
        
        tasks.sort(key = lambda x:x[0])
        res,minHeap = [],[]
        
        i, time = 0, tasks[0][0]
        while minHeap or i < len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i +=1

            if not minHeap:
                time = tasks[i][0]

            else:
                tmp = heapq.heappop(minHeap)
                procTime = tmp[0]
                res.append(tmp[1])
                time += procTime
        return res
