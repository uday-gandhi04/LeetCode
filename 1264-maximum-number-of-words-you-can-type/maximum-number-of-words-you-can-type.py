class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text=text.split()
        out=len(text)
        for word in text:
            for ch in word:
                if ch in brokenLetters:
                    out-=1
                    break
        
        return out

        