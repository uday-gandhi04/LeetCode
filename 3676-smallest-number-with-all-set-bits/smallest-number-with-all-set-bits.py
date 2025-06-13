class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while True:
            if pow(2,i)>n:
                return pow(2,i)-1
            i+=1
