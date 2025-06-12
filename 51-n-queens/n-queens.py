class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        arr=[-1]*n
        self.flag=False
        def check(idx):
            curr=arr[idx]
            for i in range(idx):
                if arr[i]==curr or arr[i]+(idx-i)==curr or arr[i]-idx+i==curr:
                    return False
                
            return True

        out=[]
        def backtrack(i):
            if i==n:
                temp=[]
                for j in range(n):
                    s=('.'*(arr[j]))+'Q'+('.'*(n-arr[j]-1))
                    temp.append(s)
                out.append(temp)
                
                return
            
            for x in range(n):
                arr[i]=x
                if not check(i):
                    continue
                backtrack(i+1)
                arr[i]=-1

        
        backtrack(0)

        return out
            
                



