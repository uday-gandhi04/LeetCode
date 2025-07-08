class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        x=float('inf')
        out=0
        for i in range(n):
            x=min(x,prices[i])
            out=max(out, prices[i]-x)
        
        return out
        