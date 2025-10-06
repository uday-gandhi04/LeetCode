class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # set of nodes that have already been visited so do not need to be revisited
        visited = set()
        # min-heap for storing the time/max height along the path, and the current coordinates
        min_heap = [[grid[0][0], 0, 0]]
        # directions that can be travelled in from a square
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # add the start coordinate to the visited set
        visited.add((0,0))

        # bfs with Djikstra's algorithm
        while min_heap:
            # pop the current minimum time and coordinates closest to the target
            time, r, c = heapq.heappop(min_heap)
            
            # if the end of the grid has been reached, the time can be returned
            if r == n-1 and c == n-1:
                return time
            
            # bfs exploring the surrounding squares
            for dr, dc in directions:
                # neighbouring square's coordinates
                nr, nc = r + dr, c + dc

                # if the square has been visited or is off the grid, skip the square
                if (nr < 0 or nr == n or nc < 0 or nc == n or (nr,nc) in visited):
                    continue
                
                # add square to the visited set
                visited.add((nr,nc))
                # push the path's max time and current coordinates to the min-heap
                heapq.heappush(min_heap, [max(time, grid[nr][nc]), nr, nc])