class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prevFlag = Solution.isEven(nums[0])
        for i in range(1,len(nums)):
            currFlag = Solution.isEven(nums[i])
            if prevFlag == currFlag:
                return False
            prevFlag = currFlag
        return True

    def isEven(num):
        if num%2 == 0:
            return True
        return False
