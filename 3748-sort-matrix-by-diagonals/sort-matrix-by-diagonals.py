class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(grid)
        arr1=[]
        arr2=[]

        for i in range(n-1,-1,-1):
            temp=[]
            j=0
            while j<n and i+j<n:
                temp.append(grid[i+j][j])
                j+=1

            arr1.append(temp)

        for i in range(n-1,0,-1):
            temp=[]
            j=0
            while j<n and i+j<n:
                temp.append(grid[j][i+j])
                j+=1

            arr2.append(temp)
        
        for a in arr1:
            a.sort(reverse=True)
        
        for a in arr2:
            a.sort()
        

        x=len(arr1)
        for i in range(n-1,-1,-1):
            temp=arr1[x-i-1]
            j=0
            while j<n and i+j<n:
                grid[i+j][j]=temp[j]
                j+=1
        
        x=len(arr2)
        for i in range(n-1,0,-1):
            temp=arr2[x-i]
            j=0
            while j<n and i+j<n:
                grid[j][i+j]=temp[j]
                j+=1
        
        return grid
        