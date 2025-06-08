class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out=[]

        def dfs(curr,n):
            if curr>n:
                return 

            out.append(curr)            
            for i in range(10):
                dfs(curr*10+i,n)
            return 
        
        for i in range(9):
            dfs(i+1,n)

        return out