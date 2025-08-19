class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=0
        count=0
        out=0
        for num in nums:
            if num==0:
                count=count+i+1
                i+=1
            else:
                out+=count
                count=0
                i=0
        
        return out+count
        