class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top=0
        bottom=len(grid)-1
        left=0
        right=len(grid[0])-1

        while top<len(grid):
            for i in grid[top]:
                if i==1:
                    break
            else:
                top+=1
                continue
            break

        while bottom>-1:
            for i in grid[bottom]:
                if i==1:
                    break
            else:
                bottom-=1
                continue
            break
        
        while left<len(grid[0]):
            for i in range(len(grid)):
                if grid[i][left]==1:
                    break
            else:
                left+=1
                continue
            break
        
        while right>-1:
            for i in range(len(grid)):
                if grid[i][right]==1:
                    break
            else:
                right-=1
                continue
            break
        
        bottom+=1
        right+=1
        return (bottom-top)*(right-left)


        
                    