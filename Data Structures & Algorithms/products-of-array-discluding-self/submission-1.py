class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        pref, suff = [], [0]*len(nums)
        res = []
        for num in nums:
            if i == 0:
                pref.append(1*num)
            else:
                pref.append(pref[i-1]*num)
            i += 1
        print(pref)
        for j in range(len(nums) - 1 , -1, -1):
            if j == len(nums) - 1:
                suff[j] = nums[j]
            else:
                suff[j] = suff[j+1]* nums[j]
        print(suff)
        for i in range(len(nums)):
            if i == 0:
                res.append(suff[i+1])
            elif i == len(nums) - 1:
                res.append(pref[i-1])
            else:
                res.append(suff[i+1]*pref[i-1])
        return res
