class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        out=[]
        for i in range(n):
            if i<2 or (s[i]!=s[i-1] or s[i-1]!=s[i-2]):
                out.append(s[i])
        return ''.join(out)
        