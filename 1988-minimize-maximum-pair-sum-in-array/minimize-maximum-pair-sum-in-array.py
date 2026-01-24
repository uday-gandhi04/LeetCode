class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        return max([nums[i]+nums[-i-1] for i in range(len(nums)//2)])


        