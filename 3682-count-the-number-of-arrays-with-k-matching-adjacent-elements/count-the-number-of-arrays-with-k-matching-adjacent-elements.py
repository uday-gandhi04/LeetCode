class Solution(object):
    MOD = 10**9 + 7

    def mod_pow(self, a, e):
        res = 1
        while e:
            if e & 1:
                res = res * a % self.MOD
            a = a * a % self.MOD
            e >>= 1
        return res

    def prepare_fact(self, n):
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % self.MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = self.mod_pow(fact[n], self.MOD - 2)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % self.MOD
        return fact, inv_fact

    def nCr(self, n, r, fact, inv_fact):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % self.MOD * inv_fact[n - r] % self.MOD

    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        runs = n - k
        fact, inv_fact = self.prepare_fact(n)
        choose = self.nCr(n - 1, runs - 1, fact, inv_fact)
        pow_part = self.mod_pow(m - 1, runs - 1)
        return choose * m % self.MOD * pow_part % self.MOD