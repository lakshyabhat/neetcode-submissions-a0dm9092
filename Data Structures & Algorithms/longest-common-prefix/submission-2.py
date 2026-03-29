class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_w = float('inf')
        for word in strs:
            min_w = min(min_w,len(word))
        l = min_w
        start_word = strs[0]
        for i in range(1,len(strs)):
            compare_word = strs[i]
            while start_word[:l] != compare_word[:l]:
                l -= 1
        return start_word[:l]
            