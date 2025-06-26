class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def binaryToDecimal(b):
            b=b[::-1]
            dec=0
            for i in range(len(b)):
                if b[i]=='1':
                    dec+=2**i
            return dec
        
        if binaryToDecimal(s)<=k:
            return len(s)
        n=len(s)
        dic=[]
        for i in range(n):
            if s[i]=='1':
                dic.append(i)
        temp=''
        for i in dic:
            for j in range(i):
                if s[j]=='0':
                    temp+='0'
            temp=temp+s[i+1:]
            if binaryToDecimal(temp)<=k:
                return len(temp)
            temp=''
        return 0


