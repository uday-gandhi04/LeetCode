class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_even = (n + 1) // 2   # number of even positions
        n_odd = n // 2          # number of odd positions

        MOD = 10**9 + 7
        out = (pow(5, n_even, MOD) * pow(4, n_odd, MOD)) % MOD

        
        return out
        