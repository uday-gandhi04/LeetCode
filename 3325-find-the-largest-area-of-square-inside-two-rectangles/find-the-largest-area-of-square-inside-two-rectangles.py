class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        maxSquare = 0
        for i in range(n - 1):
            a, b = bottomLeft[i]
            c, d = topRight[i]
            for j in range(i + 1, n):
                aj, bj = bottomLeft[j]
                cj, dj = topRight[j]
                width = min(c, cj) - max(a, aj)
                height = min(d, dj) - max(b, bj)
                if width > 0 and height > 0:
                    square = min(width, height)
                    maxSquare = max(maxSquare, square)
        return maxSquare ** 2