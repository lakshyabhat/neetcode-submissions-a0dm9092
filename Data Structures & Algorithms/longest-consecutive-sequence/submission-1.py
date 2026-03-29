class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []
        longest = 0
        numSet = set(nums)
        for n in nums:
            curr = 1
            i = 1
            if n-1 not in numSet:
                while n+i in numSet:
                    curr += 1
                    i += 1
                longest = max(longest,curr)
        return longest



