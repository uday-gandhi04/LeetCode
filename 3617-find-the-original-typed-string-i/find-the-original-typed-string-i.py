class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        out=1

        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                out+=1
        return out