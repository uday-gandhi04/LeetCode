class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = int(math.log(n,2))+1
        return 2**base -1
        
