class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)

        root = complexity[0]
        for c in complexity[1:]:
            if c <= root:
                return 0
        # Otherwise, any order of the remaining n-1 computers works:
        ans = 1
        for i in range(1, n):
            ans = ans * i % MOD
        return ans
