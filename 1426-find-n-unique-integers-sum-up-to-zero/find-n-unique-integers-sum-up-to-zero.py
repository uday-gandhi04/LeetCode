class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out=[]
        if n%2==0:
            for i in range(1,(n/2) +1 ):
                out.extend([i,-i])
        else:
            out.append(0)
            for i in range(1,(n//2) +1 ):
                out.extend([i,-i])
        return out


        