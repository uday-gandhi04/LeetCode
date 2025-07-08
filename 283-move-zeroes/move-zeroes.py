class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        while i < n and j <n:
            while i< n-1 and nums[i]!=0:
                i+=1
            j=i+1
            while j<n and nums[j]==0:
                j+=1
            if j<n:
                nums[i],nums[j]=nums[j],nums[i]
