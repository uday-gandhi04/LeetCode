class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]

        for h in happiness:
            heapq.heappush(heap,-h)

        out=0

        for i in range(k):
            out+=max((-heapq.heappop(heap))-i,0)
        
        return out