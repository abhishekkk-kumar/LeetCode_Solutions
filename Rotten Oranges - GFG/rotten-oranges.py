class Solution:
    def orangesRotting(self, grid):
        
        def dfs(grid,r,c,time):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or 1<grid[r][c] and grid[r][c]<time:
                return 
            
            grid[r][c]=time
            
            
            dfs(grid,r-1,c,grid[r][c]+1)
            dfs(grid,r+1,c,grid[r][c]+1)
            dfs(grid,r,c-1,grid[r][c]+1)
            dfs(grid,r,c+1,grid[r][c]+1)
            
        
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c]==2:
                    dfs(grid,r,c,grid[r][c])
                    
        totalTime=2
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c]==1:
                    return -1
                totalTime=max(grid[r][c],totalTime)
        
        return totalTime-2
            
            
#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends