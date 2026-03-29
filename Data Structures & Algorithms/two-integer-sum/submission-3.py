class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,n in enumerate(nums):
            indices[n] = i
        for i,n in enumerate(nums):
            if target - n in indices and i!=indices[target - n]:
                    return [i,indices[target - n]]