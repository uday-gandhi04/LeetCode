class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        out=0
        for i in range(min(n,limit)+1):
            out+=max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return out