class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x:x[0])
        out=[intervals[0]]

        for i in range(1,len(intervals)):
            if out[-1][1]>=intervals[i][0]:
                out[-1][1]=max(out[-1][-1],intervals[i][1])
            else:
                out.append(intervals[i])
        
        return out
            

        