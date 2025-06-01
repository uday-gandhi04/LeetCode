class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        x=1

        for i in range(len(coins)):
            if coins[i]<=x:
                x+=coins[i]
            else:
                break
        return x


        