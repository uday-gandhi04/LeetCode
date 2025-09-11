class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        from collections import deque

        vowels=[]

        v=set(['A','E','I','O','U','a','e','i','o','u'])

        for ch in s:
            if ch in v:
                vowels.append(ch)

        vowels.sort()
        vowels=deque(vowels)
        
        t=""
        for ch in s:
            if ch in v:
                t+=vowels.popleft()
            else:
                t+=ch
        
        return t
        
        