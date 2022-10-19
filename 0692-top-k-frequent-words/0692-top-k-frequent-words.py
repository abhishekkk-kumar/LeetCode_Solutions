class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        
        
        l=[]
        for word in d:
            l1=[]
            l1.append(d[word])
            l1.append(word)
            l.append(l1)
        
        l.sort(key=lambda element: (-element[0], element[1]))
        
        #print(l)
        
        ans=[]
        i=0
        while k:
            ans.append(l[i][1])
            i+=1
            k-=1
        
        return ans