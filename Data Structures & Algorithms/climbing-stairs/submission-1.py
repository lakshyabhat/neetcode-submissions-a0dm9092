class Solution:
    def climbStairs(self, n: int, cache = {}) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n in cache:
                return cache[n]
            else:
                return self.climbStairs(n - 1) + self.climbStairs(n - 2)
            