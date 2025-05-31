class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        queue=deque()
        n=len(board)
        queue.append(0)
        visited=set()
        level=0
        arr=[]
        for i in range(n-1,-1,-1):
            for j in range(n):
                if (n-1-i)%2==0:
                    arr.append(board[i][j])
                else:
                    arr.append(board[i][-j-1])

        while queue:
            sz=len(queue)
            while sz:
                curr=queue.popleft()
                if curr in visited:
                    sz-=1
                    continue
                visited.add(curr)
                for i in range(1,7):
                    if curr+1==n**2:
                        return level
                    if curr+i<n**2:
                        if arr[curr+i]==-1:
                            queue.append(curr+i)
                        else:
                            queue.append(arr[curr+i]-1)
                sz-=1
            level+=1
        return -1