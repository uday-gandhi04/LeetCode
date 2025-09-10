class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        frnd_cc=set()

        for a,b in friendships:
            l1=set(languages[a-1])
            l2=set(languages[b-1])

            if not(l1 & l2):
                frnd_cc.update([a,b])
            
        from collections import Counter
        dic = Counter()

        for f in frnd_cc:
            for l in languages[f-1]:
                dic[l]+=1

        if not dic:
            return 0
        
        most_s=max(dic,key=lambda x:dic[x])
        out=0
        for f in frnd_cc:
            if most_s not in languages[f-1]:
                out+=1
        
        return out




        