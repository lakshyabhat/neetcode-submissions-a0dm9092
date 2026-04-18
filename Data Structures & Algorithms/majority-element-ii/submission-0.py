class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        l = len(nums)//3
        res = []
        for k,v in c.items():
            if v > l:
                res.append(k)
        return res