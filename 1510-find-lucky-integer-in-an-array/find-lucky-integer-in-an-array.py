class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter

        dic=Counter(arr)
        out=-1
        for key,value in dic.items():
            if key==value:
                out=max(out,key)
        return out
