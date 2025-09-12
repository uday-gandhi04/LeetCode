class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        count=0

        vowels=set(['a','e','i','o','u'])
        
        for ch in s:
            if ch in vowels:
                count+=1
        if count==0:
            return False
        return True