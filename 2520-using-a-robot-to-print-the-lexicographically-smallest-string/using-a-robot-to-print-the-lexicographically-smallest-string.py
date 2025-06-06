from collections import Counter

class Solution(object):
    def robotWithString(self, s):
        freq = Counter(s)
        stack = []
        result = []

        # Start tracking from 'a'
        min_ord = ord('a')

        for c in s:
            stack.append(c)
            freq[c] -= 1

            # Move min_ord forward if that char is not present in freq anymore
            while min_ord <= ord('z') and freq[chr(min_ord)] == 0:
                min_ord += 1

            # Pop from stack if it's <= the current minimum char left
            while stack and ord(stack[-1]) <= min_ord:
                result.append(stack.pop())

        # Add remaining stack elements
        while stack:
            result.append(stack.pop())

        return "".join(result)
