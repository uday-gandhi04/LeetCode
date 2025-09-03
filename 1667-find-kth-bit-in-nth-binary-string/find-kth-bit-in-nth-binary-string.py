class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s='0'
        
        def invert(s):
            out=''
            for i in s:
                out+= '1' if i=='0' else '0'
            
            return out[::-1]

        for i in range(1,n):
            s=s[:]+'1'+invert(s)
            if len(s)>=k:
                break

        return s[k-1]
        
