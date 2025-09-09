class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            if not('0' in str(i) or '0' in str(n-i)):
                return i,n-i



        