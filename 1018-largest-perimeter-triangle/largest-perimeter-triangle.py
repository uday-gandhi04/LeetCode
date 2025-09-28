class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)

        n=len(nums)

        for i in range(n-2):
            a,b,c=nums[i],nums[i+1],nums[i+2]
            if b+c>a:
                return a+b+c
        return 0
                    
            