Explanation
The basic idea of this solution is to keep track of the current remainder of the sum of elements in nums up to some index i when divided by k --> curr_rem. We store all previous such remainders as keys in a dictionary, remainders, with their values corresponding the the index at which we had that remainder. If the current remainder has been seen before, and it was at an index lower than i-1 then that means that the sum of the subarray containing all elements from remainders[curr_rem]+1 to i (inclusive) will be a multiple of k because the difference of the remainder before and after going through that subarray is the same. Since going through that subarray did not modify our curr_rem, we know that it must sum to a multiple of k. The reason we need to check that remainders[curr_rem] < i-1 is that we will encounter a case where remainders[curr_rem] == i-1 if nums[i] == 0. However, the subarray of elements from remainders[curr_rem]+1 to i will therefore be from i to i, meaning that it just represents one element, the nums[i] == 0. We need subarrays of length 2 or more, so we have to check this condition too. If we have not seen the curr_rem before, then we add it to remainders. We only add it if we ahve not seen curr_rem before since we want remainders[curr_rem] to point to the earliest occurrence of the remainder. The reason we start with remainders = {0: -1} is that we may encounter a time when curr_rem = 0 and if i > 0 then this means we have found a subarray such that sum(nums[:i+1]) % k == 0 --> the first i elements form a subarray which satisfies our condition, so we want to be able to check that 0 already exists in remainders to catch this case.
​
This is a lot of text, so it may be easier to see with examples:
​
Examples
​
k = 6
nums = [23,2,4,6,7]
prefix sum array =  [23, 25, 29, 35, 42]
prefix mod array = [5, 1, 5, 5, 0]
We can use the prefix mod array to figure out all subarrays which satisfy our condition. 5 is present at the 0th index of our prefix mod array, which would mean remainders[5] = 0 in our solution. That means that, when we get to index 2 and find that we have already seen a remainder of 5, we then check that the two 5s are not directly next to each other (remainders[5] < i-1) and since they aren't we know that the subarray is possible (the subarray is [2,4] since it goes from remainders[5]+1 to i, which is 1 to 2).
Even if the second 5 didn't exist, we would also be able to make the subarray from [2,4,6], since the first 5 and the last 5 are not adjacent, but we could NOT make the subarray from [6] since the last two 5s are directly next to each other. We could also use the full subarray, [23,2,4,6,7], since the last value in the mod array is 0.
​
k = 6
nums = [23,2,6,4,7]
prefix sum array =  [23, 25, 31, 35, 42]
prefix mod array = [5, 1, 1, 5, 0]
The subarray is comprised of the elements between the two 5s, so it is [2,6,4]. We could also use the full subarray since the last mod value is 0, so [23,2,6,4,7] is a valid subarray as well.
​
k = 13
nums = [23,2,6,4,7]
prefix sum array = [23, 25, 31, 35, 42]
prefix mod array = [10, 12, 5, 9, 3]
Our prefix mod array has no duplicate values and no zeroes so there is no way for us to create a subarray satisfying our condition.
​
If the explanation above and examples have still left you with some questions about the solution, please ask and I will try to explain!
​
Complexity Analysis
Since we need to look at every element in nums once in the worst case (when no subarray exists that meets our condition), the time complexity is O(N) where N == len(nums).
The only possible remainders are from 0 to K-1, so the maximum size of remainders scales with K, giving our solution a space complexity of O(K).