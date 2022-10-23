class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in nums:
            if nums.count(i)==2:
                b=i
                break
        
        sum1=0
        for i in range(1,len(nums)+1):
            sum1+=i
        #print(sum1)
        sum2=0
        
        sum2=sum(set(nums))
        
        #print(sum2)
        
        a=abs(sum2-sum1)
        
        return [b,a]