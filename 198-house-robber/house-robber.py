class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if not nums:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[-1],nums[-2])
        if n==3:
            return max(nums[1],nums[0]+nums[2])
        
        nums[2]+=nums[0]

        for i in range(3,n):
            nums[i]+=max(nums[i-2],nums[i-3])
        
        return max(nums[-1],nums[-2])
        

            
        