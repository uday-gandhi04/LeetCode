class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:(x[0],-x[1]))
        out=0

        for p in range(1,len(points)):
            for i in range(p-1,-1,-1):
                if (points[i][0]<points[p][0] and points[i][1]>=points[p][1]) or points[i][0]==points[p][0] or points[i][1]==points[p][1]:
                    for j in range(i+1,p):
                        if points[i][0]<=points[j][0]<=points[p][0] and points[i][1]>=points[j][1]>=points[p][1]:
                            break
                    else:
                        out+=1

        return out
