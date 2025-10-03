class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m,n=len(heightMap),len(heightMap[0])
        heap=[]
        visited=set()
        water=0
        for i in range(n):
            heapq.heappush(heap,(heightMap[0][i],0,i))
            heapq.heappush(heap,(heightMap[-1][i],m-1,i))
            visited.add((0,i))
            visited.add((m-1,i))
        
        for i in range(m):
            heapq.heappush(heap,(heightMap[i][0],i,0))
            heapq.heappush(heap,(heightMap[i][-1],i,n-1))
            visited.add((i,0))
            visited.add((i,n-1))
        


        directions=[(-1,0),(0,-1),(1,0),(0,1)]

        while heap:
            height,x,y=heapq.heappop(heap)
            for dx,dy in directions:
                if (x+dx,y+dy) not in visited and 0<=x+dx<m and 0<=y+dy<n:
                    if heightMap[x+dx][y+dy]<height:
                        water+=height-heightMap[x+dx][y+dy]
                    visited.add((x+dx,y+dy))
                    heapq.heappush(heap,(max(heightMap[x+dx][y+dy], height),x+dx,y+dy))
        return water



