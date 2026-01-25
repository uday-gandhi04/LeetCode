class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==1:
            return 0
        
        nums.sort()
        out=float('inf')
        for i in range(len(nums)-k+1):
            out=min(out,nums[i+k-1]-nums[i])
        
        return out

        