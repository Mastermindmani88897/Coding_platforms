class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0, 0, 0]
        l = 0
        res = 0
        n = len(s)
        
        for r in range(n):
            cnt[ord(s[r]) - 97] += 1
            
            while cnt[0] and cnt[1] and cnt[2]:
                res += n - r
                cnt[ord(s[l]) - 97] -= 1
                l += 1
        
        return res
