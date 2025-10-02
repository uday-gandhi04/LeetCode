class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        res = 0
        while True:
            if numBottles >= numExchange:
                res += numExchange
                numBottles -= numExchange - 1
                numExchange += 1
            else:
                res += numBottles
                break
        return res