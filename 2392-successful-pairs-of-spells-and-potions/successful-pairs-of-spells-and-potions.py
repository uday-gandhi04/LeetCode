class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        potions.sort()
        n=len(potions)
        pairs=[]

        for spell in spells:

            target=float(success)/spell

            idx=bisect.bisect_left(potions,target)

            if idx <n and potions[idx]>=target:
                pairs.append(n-idx)
            else:
                pairs.append(0)
        
        return pairs
        