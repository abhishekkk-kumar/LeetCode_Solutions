class Solution:
    def minDeletions(self, s: str) -> int:
        dicti = Counter(s)
        counter = 0
        ls = []
        for i, j in dicti.items():
            while(j in ls and j!= 0):
                j -= 1
                counter += 1
            ls.append(j)
        return counter