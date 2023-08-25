class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dp(a,b,c):
            
            if c == len(s3) and b == len(s2) and a==len(s1): return True
            elif c==len(s3): return False
            
            if a<len(s1) and s1[a] == s3[c] and dp(a+1,b,c+1): 
                return True
            
            if b< len(s2) and s2[b] == s3[c] and dp(a,b+1,c+1):
                return True
            
            return False
        
        return dp(0,0,0)