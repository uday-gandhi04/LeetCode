class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict 
        vow=dict.fromkeys(['a','e','i','o','u'],0)

        con=defaultdict(int)
        maxcon=0
        maxvow=0
        for ch in s:
            if ch in vow:
                vow[ch]+=1
                maxvow=max(maxvow,vow[ch])
            else:
                con[ch]+=1
                maxcon=max(maxcon,con[ch])
        
        return maxvow+maxcon
                