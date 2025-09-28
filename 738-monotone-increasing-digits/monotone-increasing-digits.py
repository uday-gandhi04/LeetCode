class Solution(object):
    def monotoneIncreasingDigits(self, n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10   # ✅ integer division
        
        digits = digits[::-1]
        length = len(digits)
        
        mark = length
        for i in range(length - 1, 0, -1):   # ✅ go right→left
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                mark = i
        
        for i in range(mark, length):   # ✅ fill rest with 9
            digits[i] = 9
        
        out = 0
        for d in digits:
            out = out * 10 + d
        return out
