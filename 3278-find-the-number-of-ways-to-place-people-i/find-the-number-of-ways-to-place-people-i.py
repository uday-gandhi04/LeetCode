class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n=len(points)
        points.sort(key=lambda x:(x[0],-x[1]))
        out=0
        
        for i in xrange(n):
            max_y=float('-inf')
            for j in xrange(i+1,n):
                if points[j][1]<=points[i][1] and  points[j][1]>max_y:
                    out+=1
                    max_y=points[j][1]
        
        return out