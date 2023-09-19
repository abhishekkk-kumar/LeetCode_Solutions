class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # l=Counter(nums)
        # for i in range (0,len(nums)):
        #     if l[nums[i]]>1:
        #         return nums[i]
        n=len(nums)-1
        seen=[0]*(n+1)
        for num in nums:
            if seen[num]:
                return num
            seen[num]=1