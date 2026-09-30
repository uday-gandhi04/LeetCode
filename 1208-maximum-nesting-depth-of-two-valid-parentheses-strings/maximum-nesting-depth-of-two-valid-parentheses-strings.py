class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        stack=[]
        out=[]
        for ch in seq:
            if ch=='(':
                stack.append(ch)
                out.append(len(stack)%2)
            else:
                out.append(len(stack)%2)
                stack.pop()
        return out
