class Solution:
    def palindromicStrings(self, n, k):
        MOD = 10**9 + 7
        ans = 0
    
        fact = [1] * (k + 1)
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i % MOD
    
        invfact = [1] * (k + 1)
        invfact[k] = pow(fact[k], MOD - 2, MOD)
    
        for i in range(k, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD
    
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD
    
        for length in range(1, n + 1):
            half = length // 2
    
            if length % 2 == 0:
                ans = (ans + comb(k, half) * fact[half]) % MOD
            else:
                ans = (ans + k * comb(k - 1, half) * fact[half]) % MOD
    
        return ans