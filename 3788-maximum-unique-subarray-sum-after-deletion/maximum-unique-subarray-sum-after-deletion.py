class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=set()
        out=0
        temp=float('-inf')
        for num in nums:
            if num not in dic and num>0:
                dic.add(num)
                out+=num
            temp=max(temp,num)

        return temp if out==0 else out