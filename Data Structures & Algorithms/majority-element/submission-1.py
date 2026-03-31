class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        l = len(nums)/2
        for k,v in count.items():
            if v>l:
                return k
        return