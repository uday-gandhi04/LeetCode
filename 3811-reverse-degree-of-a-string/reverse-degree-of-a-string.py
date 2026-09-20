class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        out=0
        for i,ch in enumerate(s):
            out+= (ord('z')-ord(ch)+1)*(i+1)
        
        return out