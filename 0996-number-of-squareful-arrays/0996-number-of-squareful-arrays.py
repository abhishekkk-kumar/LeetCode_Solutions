class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def is_square(x):
            return int(x ** 0.5) ** 2 == x

        def backtrack(path, count):
            if len(path) == len(A):
                result[0] += 1
                return

            for i, num in enumerate(A):
                if count[i] > 0:
                    if i > 0 and A[i] == A[i - 1] and count[i - 1] > 0:
                        continue

                    if len(path) == 0 or is_square(path[-1] + num):
                        count[i] -= 1
                        backtrack(path + [num], count)
                        count[i] += 1
    
        A.sort()
        result = [0]
        backtrack([], [1] * len(A))
        return result[0]
        