class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            a=0
            i=bin(i).replace("0b","")
            #print(i)
            i=str(i)
            a=i.count('1')
            ans.append(a)
            
        return ans
            
            
        