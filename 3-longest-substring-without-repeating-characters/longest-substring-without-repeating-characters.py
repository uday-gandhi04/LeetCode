class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen={}
        left=0
        max_len=0

        for right,char in enumerate(s):
            if char not in seen:
                max_len=max(max_len,right-left+1)
            else:
                if seen[char]<left:
                    max_len=max(max_len,right-left+1)
                else:
                    left=seen[char]+1
            
            seen[char]=right

        
        return max_len