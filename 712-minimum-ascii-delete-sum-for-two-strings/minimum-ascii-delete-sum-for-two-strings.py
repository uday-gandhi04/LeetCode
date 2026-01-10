class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m=len(s1)
        n=len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])

        # base case: s1 exhausted → delete remaining s2 suffix
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])

        for i in range(m-1,-1,-1):
            for j in range (n-1,-1,-1):
                if s1[i]!=s2[j]:
                    dp[i][j]=min(dp[i+1][j]+ord(s1[i]),dp[i][j+1]+ord(s2[j]))
                else:
                    dp[i][j]=dp[i+1][j+1]
        print(dp)
        return dp[0][0]