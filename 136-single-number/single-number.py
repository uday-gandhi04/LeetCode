class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from collections import Counter

        dic=Counter(nums)

        for key,value in dic.items():
            if value==1:
                return key

        