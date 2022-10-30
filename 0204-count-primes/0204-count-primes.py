class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * 2 + [True] * (n - 2)
        i = 2
        while i * i < n:
            if sieve[i]:
                for j in range(2 * i, n, i):
                    sieve[j] = False
            i += 1
        return sieve.count(True)