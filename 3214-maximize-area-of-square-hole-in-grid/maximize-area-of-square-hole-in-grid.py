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

        h=[hBars[0],hBars[0]]
        v=[vBars[0],vBars[0]]
        x,y=h

        for i in range(1,len(hBars)):
            if hBars[i]-hBars[i-1]==1:
                y=hBars[i]
            else:
                if y-x>h[1]-h[0]:
                    h=x,y
                x=hBars[i]
                y=hBars[i]
        
        if y-x>h[1]-h[0]:
            h=x,y

        x,y=v
        for i in range(1,len(vBars)):
            if vBars[i]-vBars[i-1]==1:
                y=vBars[i]
            else:
                if y-x>v[1]-v[0]:
                    v=x,y
                x=vBars[i]
                y=vBars[i]
        
        if y-x>v[1]-v[0]:
            v=x,y

        
        s=min(h[1] - h[0] + 2, v[1] - v[0] + 2)
        return s**2


        