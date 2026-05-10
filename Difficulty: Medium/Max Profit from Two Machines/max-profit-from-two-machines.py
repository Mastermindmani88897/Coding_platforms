class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)
        
        tasks = []
        
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))
        
        tasks.sort(reverse=True)
        
        profit = 0
        
        for _, ai, bi in tasks:
            
            if (ai >= bi and x > 0) or y == 0:
                profit += ai
                x -= 1
            else:
                profit += bi
                y -= 1
        
        return profit