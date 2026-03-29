class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums)+1):
            if num not in set(nums):
                return num