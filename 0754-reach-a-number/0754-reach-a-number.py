class Solution:
    def reachNumber(self, target: int) -> int:
        steps,sum1=0,0
        if target==0: return 0
        target=abs(target)
        
        while(sum1<target):
            sum1+=steps
            steps+=1
        
        while((sum1-target)%2==1):
            sum1+=steps
            steps+=1
        
        return steps-1
        