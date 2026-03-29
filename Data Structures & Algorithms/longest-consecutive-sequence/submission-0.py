class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []
        longest = 0
        for n in nums:
            curr = 1
            i = 1
            if n-1 not in set(nums):
                while n+i in set(nums):
                    curr += 1
                    i += 1
                longest = max(longest,curr)
        return longest



