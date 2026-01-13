class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        squares.sort(key=lambda x: x[1])
        eps=10**(-5)

        ymin=squares[0][1]
        ymax=squares[0][1]+squares[0][2]
        total=squares[0][2]**2
        for i in range(1,len(squares)):
            total+=squares[i][-1]**2
            ymin=min(ymin,squares[i][1])
            ymax=max(ymax,squares[i][1]+squares[i][2])

        while ymax - ymin > eps:
            yo=(ymin+ymax)/2.0

            area_below=0
            for x,y,l in squares:
                if y+l<=yo:
                    area_below+=l*l
                elif y<yo<y+l:
                    area_below+=l*(yo-y)
                elif y >= yo:
                    break
            area_above=total-area_below

            if area_below<area_above:
                ymin=yo
            else:
                ymax=yo
        return ymin
            