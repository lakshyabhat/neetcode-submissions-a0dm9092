class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                if -nums[i] > (nums[j]+nums[k]):
                    j += 1
                    continue
                elif -nums[i] < (nums[j]+nums[k]):
                    k -= 1
                    continue
                else:
                    tmp = [nums[i],nums[j],nums[k]]
                    res.add(tuple(tmp))
                    j += 1
                    k -= 1
        return [list(i) for i in set(res)]
                    