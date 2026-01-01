class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=digits[::-1]
        out=[]

        x=digits[0]+1
        carry=x//10
        x=x%10

        out.append(x)

        for d in digits[1:]:
            x=d+carry
            carry=x//10
            x=x%10
            out.append(x)
        
        if carry:
            out.append(carry)
        
        return out[::-1]



        