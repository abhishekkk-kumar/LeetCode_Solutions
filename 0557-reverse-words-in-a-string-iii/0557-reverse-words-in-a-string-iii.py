class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        s1=""
        l=s.split()
        for word in l:
            s1+=word[::-1]+" "
        
        return s1.rstrip()