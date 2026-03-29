class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if target - n not in d:
                d[n] = i
            else:
                return [d[target - n], i]
        return