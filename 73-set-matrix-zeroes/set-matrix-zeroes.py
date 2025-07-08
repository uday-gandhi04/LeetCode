class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m= len(matrix)
        n= len(matrix[0])

        firstrow=False
        firstcol=False

        for i in range(n):
            if matrix[0][i]==0:
                firstrow=True
                break
        for i in range(m):
            if matrix[i][0]==0:
                firstcol=True
                break
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if firstrow:
            for i in range(n):
                matrix[0][i]=0
        if firstcol:
            for i in range(m):
                matrix[i][0]=0

                
        