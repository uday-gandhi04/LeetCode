class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        right=sum(nums)
        left=0
        out=[]
        for i in range(n):
            right-=nums[i]
            out.append(abs(right-left))
            left+=nums[i]


        return out

