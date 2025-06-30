class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        summ=sum(nums)

        for i in range(n-1,-1,-1):
            summ-=nums[i]
            if summ>nums[i]:
                return summ+nums[i]
        return -1

            

            