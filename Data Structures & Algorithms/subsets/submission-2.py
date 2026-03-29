class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        currSet = []
        i = 0

        def helper(i):
            if i == len(nums):
                sub.append(currSet.copy())
                return
            
            currSet.append(nums[i])
            helper(i+1)
            currSet.pop()
            
            helper(i+1)

        helper(i)
            
        return sub

