class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        x=float('inf')
        out=0
        for i in range(1,n+1):
            x=min(x,prices[i-1])
            out=max(out, prices[i-1]-x)
        
        return out
        