class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[float('inf')]*(n+1)

        for i in range(1,n+1):
            dp[i]=min(dp[i-1],prices[i-1])

        out=0

        for i in range(n):
            out=max(out, prices[i]-dp[i+1])
        
        return out
        