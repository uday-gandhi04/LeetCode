class Solution(object):
    def answerString(self, word, k):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if k==1:
            return word
        n=len(word)
        x=max(word)
        out=""
        arr=[]
        temp=out
        for i in range(n):
            if word[i]==x:
                arr.append(i)
        window=n-k+1
        for i in arr:
            out=max(out,word[i:i+window])
        return out