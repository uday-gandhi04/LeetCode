class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[-1]*n
        def check(idx):
            curr=arr[idx]
            for i in range(idx):
                if arr[i]==curr or arr[i]+(idx-i)==curr or arr[i]-idx+i==curr:
                    return False
                
            return True

        self.out=0
        def backtrack(i):
            if i==n:
                self.out+=1
                
                return
            
            for x in range(n):
                arr[i]=x
                if not check(i):
                    continue
                backtrack(i+1)
            return 

        
        backtrack(0)

        return self.out
            
        