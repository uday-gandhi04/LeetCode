class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        out=s[:2]
        for i in range(2,n):
            if not (s[i]==s[i-1] and s[i-1]==s[i-2]):
                out+=s[i]
        return out
        