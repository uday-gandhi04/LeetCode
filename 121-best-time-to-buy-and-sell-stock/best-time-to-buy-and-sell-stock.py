class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x=float('inf')
        out=0
        for price in prices:
            if price <x:
                x=price
            elif price-x>out:
                out=price-x
        
        return out
        