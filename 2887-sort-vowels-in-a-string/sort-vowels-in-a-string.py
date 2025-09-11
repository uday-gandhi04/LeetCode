class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowels=[]

        v=set(['A','E','I','O','U','a','e','i','o','u'])

        for ch in s:
            if ch in v:
                vowels.append(ch)

        vowels.sort()
        x=0
        for i in range(len(s)):
            if s[i] in v:
                s[i]=vowels[x]
                x+=1
        
        return ''.join(s)
        
        