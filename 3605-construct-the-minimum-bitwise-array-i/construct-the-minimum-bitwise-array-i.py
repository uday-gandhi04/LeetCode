class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans=[]

        for num in nums:
            for i in range(num+1):
                if i | i+1 == num:
                    ans.append(i)
                    break
            else:
                ans.append(-1)
        return ans