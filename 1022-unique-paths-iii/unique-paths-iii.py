class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        start=[]
        block=set()
        goal=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    start=[i,j]
                if grid[i][j]==2:
                    goal=[i,j]
                if grid[i][j]==-1:
                    block.add((i,j))

        pathlen=n*m-len(block)
        out=[0]

        def backtrack(i,j,l):

            if i==goal[0] and j==goal[1]:
                if l==pathlen:
                    out[0]+=1
                return 
            
            if (i,j) in block or i<0 or j<0 or i>=m or j>=n :
                return
            block.add((i,j))
            
            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            
            for dx,dy in directions:
                backtrack(i+dx,j+dy,l+1)

            block.remove((i,j))
        
        backtrack(start[0],start[1],1)
            
        return out[0]
            
                

        