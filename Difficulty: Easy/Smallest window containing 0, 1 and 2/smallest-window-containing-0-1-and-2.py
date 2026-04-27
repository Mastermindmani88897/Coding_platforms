class Solution:
    def smallestSubstring(self, s):
        count = {'0':0, '1':0, '2':0}
        l = 0
        res = float('inf')
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            while count['0'] > 0 and count['1'] > 0 and count['2'] > 0:
                res = min(res, r - l + 1)
                count[s[l]] -= 1
                l += 1
        
        return res if res != float('inf') else -1