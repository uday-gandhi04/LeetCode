class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        x=0

        for i in range(len(coins)):
            if coins[i]<=x+1:
                x+=coins[i]
            else:
                break
        return x+1


        