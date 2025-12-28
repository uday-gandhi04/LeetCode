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
            if happiness[i]-i>0:
                out+=happiness[i]-i
            else:
                break
        
        return out