class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        n=len(nums)
        mn=nums[0]
        out=1
        for i in range(n):
            if nums[i]-mn>k:
                mn=nums[i]
                out+=1
        return out

            

        