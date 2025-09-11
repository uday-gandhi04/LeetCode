class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels=[]

        v=set(['A','E','I','O','U','a','e','i','o','u'])

        for ch in s:
            if ch in v:
                vowels.append(ch)

        vowels.sort()
        x=0
        t=""
        for ch in s:
            if ch in v:
                t+=vowels[x]
                x+=1
            else:
                t+=ch
        
        return t
        
        