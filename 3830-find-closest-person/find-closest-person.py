class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        a=abs(z-x)
        b=abs(z-y)
        if a==b:
            return 0
        
        return 1 if a<b else 2