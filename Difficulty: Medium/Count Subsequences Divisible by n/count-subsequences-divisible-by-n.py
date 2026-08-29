class Solution:
    def countSubsequences(self, s, n):
        MOD = 10**9 + 7
        dp = [0] * n
    
        for ch in s:
            d = int(ch)
            new = dp[:]
    
            new[d % n] = (new[d % n] + 1) % MOD
    
            for r in range(n):
                nr = (r * 10 + d) % n
                new[nr] = (new[nr] + dp[r]) % MOD
    
            dp = new
    
        return dp[0]