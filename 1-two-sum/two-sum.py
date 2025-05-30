class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set1=set()

        for i in nums:
            set1.add(target-i)
        
        for i in range(len(nums)):
            if nums[i] in set1 and i!=nums.index(target-nums[i]) :
                    return [i,nums.index(target-nums[i])]