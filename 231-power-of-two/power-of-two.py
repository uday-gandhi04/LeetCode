import math

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        x = math.log(n, 2)
        return abs(x - round(x)) < 1e-10
