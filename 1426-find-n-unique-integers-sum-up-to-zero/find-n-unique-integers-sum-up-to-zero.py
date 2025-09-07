class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out=[]
        for i in range(1,(n//2) +1 ):
            out.extend([i,-i])
        if n%2!=0:
            out.append(0)
        return out


        