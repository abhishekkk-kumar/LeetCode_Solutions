class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #return nums.index(max(nums)) 
        
        l=0
        r=len(nums)-1
        
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[m+1]:
                l=m+1
            else:
                r=m
        return r