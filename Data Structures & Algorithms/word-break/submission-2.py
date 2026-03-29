class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[s[:i+1]] = True
            else:
                for r in range(i,-1,-1):
                    if s[0:r] in dp and s[r:i+1] in wordDict and dp[s[0:r]]:
                        dp[s[0:i+1]] = True
                        break
                if s[0:i+1] not in dp:
                    dp[s[0:i+1]] = False
        return dp[s]
                        
            
