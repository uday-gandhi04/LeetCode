class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        out=0
        for sentence in sentences:
            out=max(out,sentence.count(' ')+1)
        
        return out
        