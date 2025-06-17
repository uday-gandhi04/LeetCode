class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out=[]

        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]>k:
                return []
            out.append([nums[i],nums[i+1],nums[i+2]])

        return out