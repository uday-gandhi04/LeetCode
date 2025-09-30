class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while len(nums)>1:
            temp=[]

            for i in range(len(nums)-1):
                t=(nums[i]+nums[i+1])%10
                temp.append(t)
            nums=temp
        return nums[0]
        