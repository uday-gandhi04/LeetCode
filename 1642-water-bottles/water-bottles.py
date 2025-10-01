class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        out=numBottles

        nb=numBottles

        while nb>=numExchange:
            ex=nb/numExchange
            out+=ex
            nb=(nb-ex*numExchange)+ex

        return out
            
        