class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)

        for i,ch in enumerate(s):
            if ch=='6':
                return int(s[:i]+'9'+s[i+1:])
        return num
        