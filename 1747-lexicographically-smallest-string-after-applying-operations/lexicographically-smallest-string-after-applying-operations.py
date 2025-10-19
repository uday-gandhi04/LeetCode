class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """

        visited=set()
        out=[s]
        def dfs(s):
            if s in visited:
                return
            
            out[0]=min(out[0],s)
            visited.add(s)
            temp=list(s)
            for i in range(1,len(s),2):    
                x=int(s[i])
                temp[i]=str(x+a)[-1]
            dfs(''.join(temp))
            dfs(s[-b:]+s[:-b])
        
        dfs(s)
        return out[0]
       