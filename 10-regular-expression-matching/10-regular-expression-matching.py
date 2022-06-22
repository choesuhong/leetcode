class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [(len(p)+1)*[False] for _ in range(len(s)+1)]
        
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[0][i+1] = dp[0][i-1] and p[i] =='*'
        
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]==s[i] or p[j]=='.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j]=='*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[i+1][j+1] = (dp[i+1][j] or dp[i+1][j-1] or dp[i][j+1])
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
        
        return dp[-1][-1]
                    