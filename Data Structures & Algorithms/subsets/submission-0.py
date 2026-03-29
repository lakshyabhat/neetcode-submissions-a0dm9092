class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        currSet = []
        i = 0

        def helper(nums,sub,currSet,i):
            if i == len(nums):
                sub.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            helper(nums,sub,currSet,i+1)
            currSet.pop()
            
            helper(nums,sub,currSet,i+1)

        helper(nums,sub,currSet,i)
            
        return sub

