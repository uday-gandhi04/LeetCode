class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        out=0
        count=0
        minn=float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<=0:
                    out-=matrix[i][j]
                    count^=1
                    minn=min(minn,-matrix[i][j])
                else:
                    out+=matrix[i][j]
                    minn=min(minn,matrix[i][j])
        
        if count:    
            out-=(2*minn)
        
        return out
            

                    
        