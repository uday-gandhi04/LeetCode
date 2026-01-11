class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        out = 0

        for i in range(m):
            # Build histogram heights
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest Rectangle in Histogram
            stack = [-1]  # sentinel
            for j in range(n + 1):
                curr = heights[j] if j < n else 0

                while stack[-1] != -1 and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    out = max(out, h * w)

                stack.append(j)

        return out

