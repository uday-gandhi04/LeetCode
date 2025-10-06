class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)

        visited=set()

        best_peak=[[float('inf')]*n for _ in range(n)]

        def backtracking(i, j, peak):
            if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited:
                return float('inf')

            peak = max(peak, grid[i][j])  # <-- Move this up first!

            if peak >= best_peak[i][j]:
                return float('inf')
            best_peak[i][j] = peak

            if i == n - 1 and j == n - 1:
                return peak

            visited.add((i, j))
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            out = float('inf')
            for dx, dy in directions:
                temp = backtracking(i + dx, j + dy, peak)
                out = min(out, temp)
            visited.remove((i, j))
            return out

        
        return backtracking(0,0,grid[0][0])
                
            

        