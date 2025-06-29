class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        def beauty(st,dic):
            temp=max(dic)
            x=temp
            for i in dic:
                if i!=0:
                    x=min(x,i)

            return temp-x
        out=0
        for i in range(n-2):
            dic=[0]*26
            dic[ord(s[i])-ord('a')]+=1
            dic[ord(s[i+1])-ord('a')]+=1
            for j in range(i+2,n):
                dic[ord(s[j])-ord('a')]+=1
                out+=beauty(s[i:j+1],dic)
        return out

