class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        prefix=[0]*(n+1)

        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        out=nums[0]+nums[1]

        for i in range(n-1,-1,-1):
            if prefix[i]>nums[i] and prefix[i+1]>out: 
                return prefix[i+1]
        return -1

            

            