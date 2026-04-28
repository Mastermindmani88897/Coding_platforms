class Solution:
    def longestSubstr(self, s, k):
        count = [0] * 26
        left = 0
        maxf = 0
        res = 0
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            maxf = max(maxf, count[idx])
            
            while (right - left + 1) - maxf > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res