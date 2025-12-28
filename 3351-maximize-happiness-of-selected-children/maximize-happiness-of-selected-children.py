class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        out=0

        happiness.sort(reverse=True)

        for i in range(k):
            out+=max(happiness[i]-i,0)
        
        return out