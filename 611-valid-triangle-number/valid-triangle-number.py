class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n=len(nums)        

        out=0

        for i in range(n-2):
            for j in range(i+1,n-1):
                x=nums[i]+nums[j]

                idx=bisect.bisect_right(nums,x-1,j+1,n)

                out+=idx-j-1
        return out
        