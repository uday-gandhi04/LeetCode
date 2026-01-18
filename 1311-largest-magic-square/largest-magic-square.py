class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check(col,row,dia):
            for i in range(1,len(col)):
                if col[i-1]!=col[i] or row[i-1]!=row[i]:
                    return False
            
            return dia[0]==dia[1]==row[0]==col[0]

        m,n=len(grid),len(grid[0])
        k=min(m,n)

        while k>0:
            for i in range(m-k+1):
                for j in range(n - k + 1):
                    row = [0] * k
                    col = [0] * k
                    dia = [0, 0]

                    for r in range(k):
                        for c in range(k):
                            val = grid[i + r][j + c]
                            row[r] += val
                            col[c] += val

                        dia[0] += grid[i + r][j + r]
                        dia[1] += grid[i + r][j + (k - 1 - r)]

                    if check(col, row, dia):
                        return k
            k-=1
        
        return 1
                    

                            
                            

