class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        dic=Counter(s)
        a1=0
        a2=float('inf')

        for value in dic.values():
            if value%2==0:
                a2=min(a2,value)
            else:
                a1=max(a1,value)
        
        return a1-a2
