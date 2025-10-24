class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(x):
            digits=[int(i) for i in str(x)]

            freq=[0]*7
            for digit in digits:
                if digit>6:
                    return False
                freq[digit]+=1
            
            for i in range(7):
                if freq[i]==0:
                    continue
                if freq[i]!=i:
                    return False
            return True

        while True:
            n+=1
            if check(n):
                return n

        
