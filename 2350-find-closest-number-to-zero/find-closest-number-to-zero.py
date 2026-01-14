class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        out=nums[0]
        dist=float('inf')

        for num in nums:
            if abs(num)<dist:
                out=num
                dist=abs(num)
            elif abs(num)==dist:
                out=max(out,num)
        return out
