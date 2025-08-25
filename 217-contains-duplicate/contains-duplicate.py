class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sett=set(nums)

        return True if len(sett)!=len(nums) else False
        