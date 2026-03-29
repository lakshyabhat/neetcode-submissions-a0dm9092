class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,curr,t):

            if i >= len(nums) or t > target:
                return 
            if  t == target:
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i, curr , t+nums[i])
            curr.pop()
            dfs( i+1 , curr ,t)
        
        dfs(0,[],0)
        return res
    
