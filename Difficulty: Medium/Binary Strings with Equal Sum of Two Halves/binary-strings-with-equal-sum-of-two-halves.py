class Solution:
    def computeValue(self, n):
        MOD = 1000000007

        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        num = fact[2 * n]
        den = (fact[n] * fact[n]) % MOD

        return (num * pow(den, MOD - 2, MOD)) % MOD