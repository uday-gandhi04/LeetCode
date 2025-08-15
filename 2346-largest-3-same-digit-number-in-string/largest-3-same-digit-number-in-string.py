class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        n=len(num)
        out=float('-inf')
        x=""
        for i in range(2,n):
            if num[i]==num[i-1]==num[i-2]:
                temp=num[i-2:i+1]
                out=max(out,int(temp))
                if int(temp)==out:
                    x=temp
        
        return x

        