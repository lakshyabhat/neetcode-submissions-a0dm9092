class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trav = {}
        for i,num in enumerate(nums):
            if (target - num) in trav:
                return [trav[target-num],i]
            else:
                trav[num] = i
        return

