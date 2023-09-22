class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        combined = arr1 + arr2
        combined.sort()

        if len(combined) % 2 == 1:
            return combined[len(combined) // 2]
        else:
            return (combined[len(combined) // 2 - 1] + combined[len(combined) // 2]) / 2

        