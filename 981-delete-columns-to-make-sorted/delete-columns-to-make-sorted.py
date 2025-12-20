class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        out=0

        n=len(strs[0])

        for i in range(n):
            for j in range(1,len(strs)):
                if strs[j][i]<strs[j-1][i]:
                    out+=1
                    break

        return out