class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1=list(map(int,version1.split('.')))
        v2=list(map(int,version2.split('.')))

        

        n1=len(v1)
        n2=len(v2)

        if n1<n2:
            for i in range(n2-n1):
                v1.append(0)
        
        if n2<n1:
            for i in range(n1-n2):
                v2.append(0)
        
        for i in range(max(n1,n2)):
            if v1[i]>v2[i]:
                return 1
            if v2[i]>v1[i]:
                return -1
        
        return 0
        
        