class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    m = m*nums[j]
            res.append(m)
            m = 1
        return res
