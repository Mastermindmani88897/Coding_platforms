class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        
        # Precompute Catalan numbers up to n
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        res = []
        
        for x in arr:
            left = sum(1 for v in arr if v < x)
            right = sum(1 for v in arr if v > x)
            
            res.append(dp[left] * dp[right])
        
        return res