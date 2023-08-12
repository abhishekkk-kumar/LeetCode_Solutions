class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        @lru_cache(maxsize=None)
        def dfs(i,j):
            # reached target
            if i==ROWS-1 and j==COLS-1:
                return 1
            
            # out of bounds OR obstacle encountered
            if i>=ROWS or j>=COLS or obstacleGrid[i][j] == 1:
                return 0
            
            # performing DFS
            return dfs(i+1,j) + dfs(i,j+1)

        # start position
        return dfs(0,0)