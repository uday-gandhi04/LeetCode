class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels=set(['a','e','i','o','u'])
        
        for ch in s:
            if ch in vowels:
                return True
        return False
        