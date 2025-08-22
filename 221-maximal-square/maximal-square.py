class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        rows=len(matrix)
        col=len(matrix[0])

        dp=[[0]*(col+1) for _ in range(rows+1)]
        out=0
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j],dp[i+1][j],dp[i][j+1])+1

                    out=max(out,dp[i+1][j+1])
        
        return out**2


