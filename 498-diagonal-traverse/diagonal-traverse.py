class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n=max(len(mat),len(mat[0]))
        arr=[[] for _ in range((2*n)-1)]

        print(arr)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr[i+j].append(mat[i][j])
        
        out=[]

        flag=True
        for a in arr:
            if not flag:
                flag=True
                out.extend(a[:])
            else:
                flag=False
                out.extend(a[::-1])
        
        return out

        