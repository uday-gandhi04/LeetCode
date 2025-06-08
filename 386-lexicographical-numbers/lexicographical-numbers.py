class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out=[]

        def dfs(curr):
            out.append(curr)            
            for i in range(10):
                nxt=curr*10+i
                if nxt<=n:
                    dfs(nxt)
                else:
                    return 
            return 
        
        for i in range(1,10):
            if i<=n:
                dfs(i)
            else:
                break

        return out