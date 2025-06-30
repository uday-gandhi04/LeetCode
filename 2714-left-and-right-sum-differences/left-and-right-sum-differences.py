class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        leftSum=[0]*n
        rightSum=[0]*n

        for i in range(1,n):
            leftSum[i]=leftSum[i-1]+nums[i-1]
            rightSum[n-i-1]=rightSum[n-i]+nums[n-i]
        
        out=[]

        for i in range(n):
            out.append(abs(leftSum[i]-rightSum[i]))

        return out

