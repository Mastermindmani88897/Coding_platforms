class Solution:
    def findExtra(self, a, b):
        n = min(len(a), len(b))
        
        for i in range(n):
            if a[i] != b[i]:
                return i
        
        return n
