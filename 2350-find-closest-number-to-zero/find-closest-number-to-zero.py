class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        out=nums[0]
        
        for num in nums:
            if abs(num)<abs(out):
                out=num
            elif abs(num)==abs(out) and num>out:
                out=num
        return out
