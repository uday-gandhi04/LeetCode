class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        freeTime=[startTime[0]-0]
        n=len(startTime)
        for i in range(n-1):
            temp=startTime[i+1]-endTime[i]
            freeTime.append(temp)
        
        freeTime.append(eventTime-endTime[-1])
        m=len(freeTime)
        wind=min(k+1,m)
        summ=sum(freeTime[0:wind])
        out=summ
        for i in range(1,m-wind+1):
            summ=summ-freeTime[i-1]+freeTime[i+wind-1]
            out=max(out,summ)
        return out

        