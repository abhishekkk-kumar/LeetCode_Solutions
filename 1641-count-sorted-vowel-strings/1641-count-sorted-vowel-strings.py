        #                     a   e   i   o   u
        # Symbol/Value of n   
        #       n=1           1   1   1   1   1
        #       n=2           5   4   3   2   1
        #       n=3           15  10  6   3   1
        #       n=4           35  20  10  4   1 
class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = [1, 1, 1, 1, 1]  # create a list of size 5
        for i in range(2, n + 1):  # start from the 3rd index
            for j in range(3, -1, -1):  # add the value from the 2nd index
                ans[j] += ans[j + 1]
        ret = 0
        for a in ans:
            ret += a
        return ret
