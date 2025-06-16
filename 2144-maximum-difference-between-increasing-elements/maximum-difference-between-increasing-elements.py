class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                min_val = nums[i]  # update min_val only if nums[i] is smaller

        return max_diff
