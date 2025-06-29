class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[]
        n=len(nums)

        for i in range(0,n,2):
            freq=nums[i]
            val=nums[i+1]
            for j in range(freq):
                out.append(val)
        return out
        