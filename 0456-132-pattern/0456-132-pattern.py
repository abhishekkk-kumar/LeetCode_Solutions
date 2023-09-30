class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        not_found = False
        n = len(nums)
        if n < 3:
            return not_found  

        # Store the minimum element to the left of each element.
        min_left = [0] * n  
        min_left[0] = nums[0]

        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], nums[i])

        # Use a stack to store potential '3' candidates (nums[j]).
        stk = []  

        for j in range(n - 1, -1, -1):
            # We found a potential '3'.
            if nums[j] > min_left[j]:  
                while stk and stk[-1] <= min_left[j]:
                    # Remove elements that can't be '2'.
                    stk.pop()  
                if stk and stk[-1] < nums[j]:
                    # We found a '132' pattern.
                    return True  
                # Add nums[j] as a potential '2'.
                stk.append(nums[j])  

                
        return not_found  