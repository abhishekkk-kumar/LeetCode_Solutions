class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            #print(row)
            if row[-1] >= target:
                #print(row[-1])
                return target in row
        return False
                
                