class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        out=[]
        x=0
        for bit in nums:
            x=2*x+bit
            out.append(x%5==0)
        return out


        