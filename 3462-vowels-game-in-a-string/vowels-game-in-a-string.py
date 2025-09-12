class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vow=['a','e','i','o','u']

        for v in vow:
            if(v in s):
                return True
        return False