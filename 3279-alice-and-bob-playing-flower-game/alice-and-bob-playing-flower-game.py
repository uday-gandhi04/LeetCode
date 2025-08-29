class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n_even=n/2 if ((n ^ 1) == (n + 1)) else math.floor(n/2)
        n_odd=n-n_even

        m_even=m/2 if ((m ^ 1) == (m+ 1)) else math.floor(m/2)
        m_odd=m-m_even

        return int(n_even*m_odd+n_odd*m_even)

