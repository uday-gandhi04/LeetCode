class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[]

        for i in range(0,len(nums),2):
            out.extend([nums[i+1]]*nums[i])
        return out
        