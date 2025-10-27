class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        cam=[]

        for s in bank:
            c=s.count('1')
            if c :
                cam.append(c)
            
        out=0

        if len(cam)<=1:
            return 0
        
        for i in range(len(cam)-1):
            out+=cam[i]*cam[i+1]
        return out
            
        