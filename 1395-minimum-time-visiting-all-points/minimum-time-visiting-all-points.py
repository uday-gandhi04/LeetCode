class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def chebyshev_distance(point1, point2):
            return max(abs(a - b) for a, b in zip(point1, point2))
        
        out=0

        for i in range(1,len(points)):
            out+=chebyshev_distance(points[i-1],points[i])
        return out        