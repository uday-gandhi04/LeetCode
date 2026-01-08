class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m=len(nums1)
        n=len(nums2)
        dp=[[float('-inf')]*(n+1) for _ in range (m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=max(nums1[i]*nums2[j]+max(0,dp[i+1][j+1]),dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]

