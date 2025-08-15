class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if math.log(n)/math.log(4)==int(math.log(n)/math.log(4)):
            return True
        return False


        