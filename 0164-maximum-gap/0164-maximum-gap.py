class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        
        
        #print(nums)
        ans=0
        for i in range(len(nums)-1):
            diff=nums[i+1]-nums[i]
            ans=max(ans,diff)
        
        return ans
            