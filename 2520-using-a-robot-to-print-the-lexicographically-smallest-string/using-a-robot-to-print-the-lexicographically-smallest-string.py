class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        freq=Counter(s)
        stack=[]
        p=[]

        def minchar():
            for i in range(26):
                idx=chr(ord('a')+i)
                if freq[idx]!=0:
                    return idx
            return 'a'

        for i in s:
            stack.append(i)
            freq[i]-=1
            while stack and stack[-1]<=minchar():
                p.append(stack.pop())
        
        while stack:
            p.append(stack.pop())
        
        return "".join(p)
