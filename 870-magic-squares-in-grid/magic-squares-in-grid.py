class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m=len(grid)
        n=len(grid[0])

        if m<3 or n<3 :
            return 0
        
        def check(col,row,dia):

            s=col[0]

            for i in range(3):
                if row[i]!=s or col[i]!=s:
                    return 0
            
            if dia[0]!=s or dia[1]!=s:
                return 0
            
            return 1
        
        out=0
        for i in range(m-2):
            for j in range(n-2):
                col=[0,0,0]
                row=[0,0,0]
                dia=[0,0]
                x=True
                hashset=set()
                for a in range(3):
                    for b in range(3):
                        row[a] += grid[i + a][j + b]
                        col[b] += grid[i + a][j + b]
                        if grid[i+a][j+b]<=0 or grid[i+a][j+b]>9 or grid[i+a][j+b] in hashset:
                            x=False
                            break
                        hashset.add(grid[i+a][j+b])
                    if not x:
                        break
                    dia[0] += grid[i + a][j + a]
                    dia[1] += grid[i + a][j + 2 - a]
                if x:
                    out+=check(col,row,dia)
            
        return out
        
        
        