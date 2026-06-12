class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n % k != 0:
            return False
        
        blocks = [s[i:i + k] for i in range(0, n, k)]
        
        freq = {}
        for b in blocks:
            freq[b] = freq.get(b, 0) + 1
        
        if len(freq) == 1:
            return True
        
        if len(freq) > 2:
            return False
        
        vals = list(freq.values())
        
        return vals[0] == 1 or vals[1] == 1