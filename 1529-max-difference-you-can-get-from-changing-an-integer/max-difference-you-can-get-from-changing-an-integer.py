class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        mx=0
        mn=0
        n=len(s)
        temp=''
        for i,ch in enumerate(s):
            if ch!='9':
                temp=s[:i]
                for j in range(i,n):
                    if s[j]==ch:
                        temp+='9'
                    else:
                        temp+=s[j]
                
                break
            else:
                temp+=ch
        mx=int(temp)
        temp=''
        for i,ch in enumerate(s):
            if ch=='1':
                temp+=ch
            else:
                if ch!='1' and i==0:
                    temp=s[:i]
                    for j in range(i,n):
                        if s[j]==ch:
                            temp+='1'
                        else:
                            temp+=s[j]
                    break
                elif ch!='0':
                    temp=s[:i]
                    for j in range(i,n):
                        if s[j]==ch:
                            temp+='0'
                        else:
                            temp+=s[j]
                    break
                else:
                    temp+=ch
        mn=int(temp)

        return mx-mn
        