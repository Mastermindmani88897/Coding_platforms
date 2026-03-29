class Solution:
    def countPartitions(self, arr, diff):
        total = sum(arr)
        
        if (total + diff) % 2 != 0:
            return 0
        
        target = (total + diff) // 2
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[target]