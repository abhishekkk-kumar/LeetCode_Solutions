class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = 1
        r = n

        while i < n:
            if ratings[i-1] == ratings[i]:
                i += 1
                continue

            u = 0
            d = 0

            while i < n and ratings[i-1] < ratings[i]:
                u += 1
                r += u
                i += 1

            while i < n and ratings[i-1] > ratings[i]:
                d += 1
                r += d
                i += 1

            r -= min(u,d)
               
        return r