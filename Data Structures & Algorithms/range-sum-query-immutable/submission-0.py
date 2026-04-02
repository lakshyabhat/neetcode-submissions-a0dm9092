class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prevSum = 0
        prefixSum = []
        for i in range(len(self.nums)):
            prevSum += self.nums[i]
            prefixSum.append(prevSum)
        if left == 0:
            return prefixSum[right]
        return prefixSum[right] - prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)