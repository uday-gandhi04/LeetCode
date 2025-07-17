class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        from collections import defaultdict
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        ans=0
        for i in range(n):
            for j in range(i):
                mod=(nums[j]+nums[i])%k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                ans = max(ans, dp[i][mod] + 1)
        return ans




        