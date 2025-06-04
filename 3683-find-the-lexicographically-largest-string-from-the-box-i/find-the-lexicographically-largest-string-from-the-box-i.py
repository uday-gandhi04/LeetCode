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
        x=sorted(word)[-1]
        out=""
        arr=[]
        temp=out
        for i in range(n):
            if word[i]==x:
                arr.append(i)
        window=n-k+1
        while window>0:
            for i in arr:
                out=max(out,word[i:i+window])
            if out==temp:
                return out
            temp=out


        return out