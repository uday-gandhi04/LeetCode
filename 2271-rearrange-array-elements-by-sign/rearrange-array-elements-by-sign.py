class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p=0
        n=1
        out=[0]*len(nums)

        for num in nums:
            if num>=0:
                out[p]=num
                p+=2
            else:
                out[n]=num
                n+=2
        return out
        