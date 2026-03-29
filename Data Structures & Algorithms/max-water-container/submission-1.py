class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContain = 0
        l, r = 0, len(heights) - 1
        while l<r:
            currContain = min(heights[l],heights[r])*(r-l)
            maxContain = max(currContain,maxContain)
            if heights[l]<heights[r]:
                l += 1
            else:
                r -=1
        return maxContain