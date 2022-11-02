class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        
        for i,v in enumerate(groupSizes):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]
                
        ret = []
        for i in d:
            for j in range(0,len(d[i]),i):
                ret.append(d[i][j:j+i])
                
        return ret
        
        