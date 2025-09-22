class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=Counter(nums)

        out=0
        currentMax=max(counter.values())

        for freq in counter.values():
            if freq==currentMax:
                out+=freq
        
        return out