class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        fullBottles=numBottles
        mt=0
        out=0

        while fullBottles:
            mt+=fullBottles
            out+=fullBottles
            fullBottles=0
            if mt>=numExchange:
                mt-=numExchange
                fullBottles=1
                numExchange+=1
        return out
        