class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int

        \(S_{n}=\frac{n}{2}(2a+(n-1)d)\) 
        """
        totalweek=n//7
        dayRemaining=n-(totalweek*7)
        out=(totalweek/2.0)*(2*28+(totalweek-1)*7)
        a=1+totalweek
        S=(dayRemaining/2.0)*(2*a + (dayRemaining-1))

        return int(out+S)