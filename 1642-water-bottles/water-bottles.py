class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        out=numBottles

        while numBottles>=numExchange:
            ex=numBottles/numExchange
            out+=ex
            numBottles=(numBottles-ex*numExchange)+ex

        return out
            
        