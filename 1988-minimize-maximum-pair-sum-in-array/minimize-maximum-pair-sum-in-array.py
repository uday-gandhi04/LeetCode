class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        out=float('-inf')

        print(nums)
        for i in range(0,n//2):
            out=max(out,nums[i]+nums[-i-1])
        
        return out


        