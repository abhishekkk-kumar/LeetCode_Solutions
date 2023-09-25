from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #print(list(Counter(t)))
        #print(list(Counter(s)))
        return list(Counter(t)-Counter(s))[0]
        