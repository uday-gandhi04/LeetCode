class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        freq = Counter(word)
        sorted_items_asc=sorted(freq.items(),key=lambda x: x[1])
        freq=dict(sorted_items_asc)
        n=len(freq)
        out=float('inf')
        temp=0
        for i in freq.keys():
            temp=0
            for j in freq.keys():
                if freq[j]<freq[i]:
                    temp+=freq[j]
                elif freq[j]>freq[i]+k:
                    temp+=freq[j]-freq[i]-k
                
            out=min(out,temp)
        return out


