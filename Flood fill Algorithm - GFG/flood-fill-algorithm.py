class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    row,col=len(image),len(image[0])
	    
	    def dfs(i,j,color,row,col,source):
	        if i<0 or i>=row or j<0 or j>=col or image[i][j]!=source:
	            return 0
	        image[i][j]=color
	        dfs(i-1,j,color,row,col,source)
	        dfs(i+1,j,color,row,col,source)
	        dfs(i,j-1,color,row,col,source)
	        dfs(i,j+1,color,row,col,source)
	   
	    if newColor==image[sr][sc]:
	       return image
	   
	    source=image[sr][sc]
	    dfs(sr,sc,newColor,row,col,source)
	    return image
		#Code here



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends