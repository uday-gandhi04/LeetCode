class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        out=[]
        x=0
        for i in range(len(nums)):
            x=2*x+nums[i]
            if x%5==0:
                out.append(True)
            else:
                out.append(False)
        return out


        