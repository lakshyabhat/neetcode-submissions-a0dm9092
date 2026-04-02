class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        postSum = 0
        prefixArr, postFixArr = [], [0 for i in range(len(nums))]
        for i in range(len(nums)):
            prefixSum += nums[i]
            postSum += nums[len(nums)-i-1]
            prefixArr.append(prefixSum)
            postFixArr[len(nums)-i-1] = postSum
            
        for i in range(len(nums)):
            if prefixArr[i] == postFixArr[i]:
                return i
        return -1
        
        
