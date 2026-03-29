class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = 0
        return min(Solution.totalCost(cost,0,i),Solution.totalCost(cost,0,i+1))
    
    def totalCost(cost,cSum,i):
        if i >= len(cost):
            return cSum
        
        cSum = cSum + cost[i]

        return min(Solution.totalCost(cost,cSum,i+1),Solution.totalCost(cost,cSum,i+2))
        


        