class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
        
        for i,num in enumerate(nums):
            if target - num in index and index[target - num] != i:
                return [i,index[target - num]]
        return []
