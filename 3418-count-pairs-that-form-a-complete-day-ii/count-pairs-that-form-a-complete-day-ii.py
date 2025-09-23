class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        
        count=0
        for i in range(len(hours)):
            hours[i]=hours[i]%24
        
        h=Counter(hours)

        for hour in hours:
            h[hour]-=1

            if hour==0:
                count+=h[0]
            elif 24-hour in h:
                count+=max(h[24-hour],0)
            
        
        return count
        
        