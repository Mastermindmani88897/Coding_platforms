class Solution:
    def validGroups(self, s):
        
        n = len(s)
        memo = {}
        
        def dfs(idx, prev_sum):
            
            if idx == n:
                return 1
            
            if (idx, prev_sum) in memo:
                return memo[(idx, prev_sum)]
            
            ans = 0
            curr_sum = 0
            
            for j in range(idx, n):
                curr_sum += int(s[j])
                
                if curr_sum >= prev_sum:
                    ans += dfs(j + 1, curr_sum)
            
            memo[(idx, prev_sum)] = ans
            return ans
        
        return dfs(0, 0)