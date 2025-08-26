class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """

        out=0
        dia=0
        for l,b in dimensions:
            d=math.sqrt(l**2+b**2)
            if d==dia:
                out=max(out,l*b)
            elif d>dia:
                dia=d
                out=l*b
        return out
                


        