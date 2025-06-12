class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        out=0
        for i in range(n):
            out=max(out,abs(nums[i%n]-nums[(i+1)%n]))
        return out
        