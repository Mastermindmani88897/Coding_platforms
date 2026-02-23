class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        if len(s) < k or needed > len(s) - k + 1:
            return False
        
        seen = set()
        mask = 0
        
        for i, ch in enumerate(s):
            mask = ((mask << 1) & (needed - 1)) | (ch == '1')
            
            if i >= k - 1:
                seen.add(mask)
                if len(seen) == needed:
                    return True
        
        return False