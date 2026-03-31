class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        l = len(nums)/2
        for k,v in count.items():
            if v>l:
                return k
        return