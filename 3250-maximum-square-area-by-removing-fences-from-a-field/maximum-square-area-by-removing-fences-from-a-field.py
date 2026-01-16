class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """

        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])
        hset=set(hFences[i]-hFences[j] for i in range(len(hFences)) for j in range(i))
        vset=set(vFences[i]-vFences[j] for i in range(len(vFences)) for j in range(i))
        
        common = hset & vset
        if not common:
            return -1
        
        side = max(common)
        return (side * side)%(10**9+7)