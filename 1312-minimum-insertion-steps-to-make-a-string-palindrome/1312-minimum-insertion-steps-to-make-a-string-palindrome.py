class Solution:
    def minInsertions(self, s: str) -> int:
        def lcs(self,s:str):
            s1=s[::-1]
            n,m=len(s),len(s1)
            dp=[[0]*(m+1) for _ in range(n+1)]
            for i in range(n):
                for j in range(m):
                    if s[i]==s1[j]:
                        dp[i+1][j+1]=dp[i][j]+1
                    else:
                        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
            return dp[-1][-1]
        
        return len(s)-lcs(self,s)