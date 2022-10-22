# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t=="":
#             return ""

#         countT,window={},{}
#         for c in t:
#             countT[c]=1+countT.get(c,0)
        
#         have,need=0,len(countT)
        
#         res,resLen=[-1,-1],float("inf")
#         l=0
        
#         for r in range(len(s)):
#             c=s[r]
#             window[c]=1+window.get(c,0)
#             if c in countT and window[c]==countT[c]:
#                 have+=1
            
#             while have==need:
#                 if(r-l+1)<resLen:
#                     res=[l,r]
#                     resLen=r-l+1
                    
#                 window[s[l]]-=1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have-=1
                
#                 l+=1
        
#         l,r=res
#         return s[l:r+1] if resLen != float("inf") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = "", float("inf")
        countS = {}

        l = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                curLen = (r - l + 1)
                if curLen < resLen:
                    resLen = curLen
                    res = s[l:r+1]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return res 
          