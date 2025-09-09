class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            a=str(i)
            b=str(n-i)
            if '0' in a or '0' in b:
                continue
            return i,n-i



        