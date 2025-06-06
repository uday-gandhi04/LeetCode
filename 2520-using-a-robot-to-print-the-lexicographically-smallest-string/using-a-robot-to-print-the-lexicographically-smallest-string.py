from collections import Counter

class Solution(object):
    def robotWithString(self, s):
        freq = Counter(s)
        stack = []
        result = []

        min_ord = ord('a')

        for c in s:
            stack.append(c)
            freq[c] -= 1

            while min_ord <= ord('z') and freq[chr(min_ord)] == 0:
                min_ord += 1

            while stack and ord(stack[-1]) <= min_ord:
                result.append(stack.pop())

        result.extend(stack[::-1])

        return "".join(result)
