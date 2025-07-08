class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos=0

        for i in range (1,len(nums)):
            if nums[pos]!=nums[i]:
                nums[pos+1]=nums[i]
                pos+=1
            
        return pos+1
