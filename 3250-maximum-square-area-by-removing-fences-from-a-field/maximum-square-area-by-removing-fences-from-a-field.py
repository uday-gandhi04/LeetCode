class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """

        hFences=[1]+hFences+[m]
        vFences=[1]+vFences+[n]
        hset=set()
        vset=set()

        for i in range(len(hFences)):
            for j in range(i):
                hset.add(abs(hFences[i]-hFences[j]))
        
        for i in range(len(vFences)):
            for j in range(i):
                vset.add(abs(vFences[i]-vFences[j]))
        
        common = hset & vset
        if not common:
            return -1
        
        side = max(common)
        return (side * side)%(10**9+7)