class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        x=0

        for i in range(len(coins)):
            v=coins[i]
            if v<=x+1:
                x=v+x
            else:
                break
        return x+1


        