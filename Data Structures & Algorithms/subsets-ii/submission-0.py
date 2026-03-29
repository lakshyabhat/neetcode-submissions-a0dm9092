class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub = []
        currSet = []
        i = 0
        nums.sort()
        def dfs(i):
            if len(nums) == i:
                sub.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            dfs(i+1)

            currSet.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i +=1
            dfs(i+1)
        
        dfs(0)
        return sub
