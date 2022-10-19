class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        l1=[]
        lis=[]
        for i in range(0,len(l)):
            l1.append(nums[l[i]:(r[i])+1])
            l1[i].sort()
        
        for q in l1:
            c=1
            for i in range(1,len(q)):
                if q[i]-q[i-1]==q[1]-q[0]:
                    c+=1
            #print(c)
            if c==len(q):
                lis.append(True)
            else:
                lis.append(False)
                
        return lis
        
        # for q in l1:
        #     q.sort()
        #     for i in range(1,len(q)):
        #         if abs(q[i]-q[i-1])
            