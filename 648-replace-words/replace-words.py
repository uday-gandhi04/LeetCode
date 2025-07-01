class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        dic=set(dictionary)

        sentence=list(sentence.split())
        out=[]
        for word in sentence:
            flag=True
            for i in range(1,len(word)+1):
                if word[:i] in dic:
                    out.append(word[:i])
                    flag=False
                    break
            if flag:
                out.append(word)
        
        return " ".join(out)



        