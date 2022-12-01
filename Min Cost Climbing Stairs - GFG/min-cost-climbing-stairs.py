#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost, N):
        #Write your code here
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        
        return min(cost[-2],cost[-1])
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        cost=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minCostClimbingStairs(cost,N))
# } Driver Code Ends