class Solution:
    def minSteps(self, m, n, d):
        from math import gcd
        
        if d > max(m, n) or d % gcd(m, n) != 0:
            return -1
        
        def solve(fromJug, toJug, d):
            fromJ = fromJug
            toJ = 0
            step = 1
            
            while fromJ != d and toJ != d:
                temp = min(fromJ, toJug - toJ)
                toJ += temp
                fromJ -= temp
                step += 1
                
                if fromJ == d or toJ == d:
                    break
                
                if fromJ == 0:
                    fromJ = fromJug
                    step += 1
                
                if toJ == toJug:
                    toJ = 0
                    step += 1
            
            return step
        
        return min(solve(m, n, d), solve(n, m, d))