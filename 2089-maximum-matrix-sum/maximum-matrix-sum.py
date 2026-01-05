class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        out=0
        count=0
        arr=[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<=0:
                    arr.append(-matrix[i][j])
                    count+=1
                else:
                    arr.append(matrix[i][j])
        
        if count%2==0:
            out+=sum(arr)
        else:
            out+=sum(arr)
            out-=(2*min(arr))
        
        return out
            

                    
        