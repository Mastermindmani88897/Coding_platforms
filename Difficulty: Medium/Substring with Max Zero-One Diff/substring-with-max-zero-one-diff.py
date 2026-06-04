class Solution:
    def maxSubstring(self, s):
        
        if '0' not in s:
            return -1
        
        curr = 0
        ans = 0
        
        for ch in s:
            val = 1 if ch == '0' else -1
            
            curr = max(val, curr + val)
            ans = max(ans, curr)
        
        return ans