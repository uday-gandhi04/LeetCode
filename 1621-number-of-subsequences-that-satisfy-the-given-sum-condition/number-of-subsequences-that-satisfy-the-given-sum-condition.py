class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        n=len(nums)
        out=0
        j = n - 1
        for i in range(n):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if j >= i:
                out += 2 ** (j - i)

        return out%(10**9+7)

            
        