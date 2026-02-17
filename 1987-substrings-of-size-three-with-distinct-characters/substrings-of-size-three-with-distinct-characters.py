class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(set(s))<3:
            return 0
        c=0
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==3:
                c=c+1
        return c
            
