class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=Counter(nums)

        out=0
        currentMax=0

        for freq in counter.values():
            if freq==currentMax:
                out+=freq
            elif freq>currentMax:
                out=freq
                currentMax=freq
        
        return out