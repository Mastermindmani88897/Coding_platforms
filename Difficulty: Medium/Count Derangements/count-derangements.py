class Solution:
    def derangeCount(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        a, b = 0, 1
        
        for i in range(3, n + 1):
            c = (i - 1) * (a + b)
            a, b = b, c
        
        return b