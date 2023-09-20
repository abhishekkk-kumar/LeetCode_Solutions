class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Init.
        n = len(nums)
        totSum = sum(nums)
        currSum = 0
        mxLen = -1
        # Sliding window.
        left = 0
        for right in range(n):
            currSum += nums[right]
            while left <= right and currSum > totSum - x:
                currSum -= nums[left]
                left += 1
            if currSum == totSum - x:
                mxLen = max(mxLen, right - left + 1)
        # Output.
        return -1 if mxLen == -1 else n - mxLen