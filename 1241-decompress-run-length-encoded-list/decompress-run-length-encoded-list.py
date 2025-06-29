class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[]

        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            for j in range(freq):
                out.append(val)
        return out
        