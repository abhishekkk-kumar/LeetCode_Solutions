class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = []
        def helper(i,k,temp):
            if k == 0:
                lst.append(list(temp))
                return
            for j in range(i,n+1):
                temp.append(j)
                helper(j+1,k-1,temp)
                temp.pop()
        helper(1,k,[])
        return lst