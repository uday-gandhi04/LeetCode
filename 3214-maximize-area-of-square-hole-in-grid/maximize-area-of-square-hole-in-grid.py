class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        hBars.sort()
        vBars.sort()

        hdiff=0
        vdiff=0
        diff=0

        for i in range(1,len(hBars)):
            if hBars[i]-hBars[i-1]==1:
                diff+=1
            else:
                hdiff=max(hdiff,diff)
                diff=0
        
        hdiff=max(hdiff,diff)
        diff=0
        for i in range(1,len(vBars)):
            if vBars[i]-vBars[i-1]==1:
                diff+=1
            else:
                vdiff=max(vdiff,diff)
                diff=0
        
        vdiff=max(vdiff,diff)

        
        s=min(hdiff,vdiff)
        return (s+2)**2


        