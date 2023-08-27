class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s=set()
        s.add((stones[0],1))
        
        
        if len(stones)>=2:
            if stones[1]!=stones[0]+1:
                return False
            
        def solve(ind,s,k):
            # print(ind,s)
            if ind==stones[-1]:
                print(ind)
                return True
            if ind not in stones or (ind,k) in s:
                return False
            s.add((ind,k))
            return solve(ind+k-1,s,k-1) or solve(ind+k,s,k) or solve(ind+k+1,s,k+1)
        
        return solve(stones[1],s,1)