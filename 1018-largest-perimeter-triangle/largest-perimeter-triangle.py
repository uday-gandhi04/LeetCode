class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)

        n=len(nums)
        area=0

        for i in range(n-2):
            a=nums[i]
            b=nums[i+1]
            c=nums[i+2]
            if a+b>c and a+c>b and b+c>a:
                return a+b+c
        return 0
                    
            