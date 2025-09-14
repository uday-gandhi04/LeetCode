class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        exact=set(wordlist)
        Lower={}
        vow="aeiouAEIOU"

        i=0
        for word in wordlist:
            x=[]
            l=word.lower()
            if l not in Lower:
                Lower[l]=i
            for ch in l:
                if ch in vow:
                    x.append('*')
                else:
                    x.append(ch)
            x=''.join(x)
            
            if x not in Lower:
                Lower[x]=i
            
            
            i+=1


        out=[]
        for querie in queries:
            if querie in exact:
                out.append(querie)
            elif querie.lower() in Lower:
                out.append(wordlist[Lower[querie.lower()]])
            else:
                x=[]
                for ch in querie:
                    if ch in vow:
                        x.append('*')
                    else:
                        x.append(ch.lower())
                x=''.join(x)

                if x in Lower:
                    out.append(wordlist[Lower[x]])
                else:
                    out.append("")
        
        return out

