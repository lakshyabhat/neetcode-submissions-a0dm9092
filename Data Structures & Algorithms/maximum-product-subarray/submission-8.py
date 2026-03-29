class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = []
        maxp = nums[0]
        for n in nums:
            a = Solution.mul(a,n)
            a.append(n)
            maxp = max(maxp,max(a))
        return maxp
    
    def mul(arr,n):
        res = []
        for a in arr:
            res.append(a*n)
        return res
            