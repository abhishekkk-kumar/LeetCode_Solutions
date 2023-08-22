class Solution:
    def convertToTitle(self, n: int) -> str:
        all_a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while n:
            n=n-1
            ans=all_a[n%26]+ans
            n=n//26
        
        return ans
        
        