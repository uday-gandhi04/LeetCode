class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prefix=0
        count=0

        for i in s:
            if i=='(':
                prefix+=1
            elif i==')':
                prefix-=1
            else:
                count+=1
            if count+prefix<0:
                return False
        
        prefix=0
        count=0
        

        for i in s[::-1]:
            if i==')':
                prefix+=1
            elif i=='(':
                prefix-=1
            else:
                count+=1
            if count+prefix<0:
                return False
        
        return True
            

        