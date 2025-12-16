class Solution(object):
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low
