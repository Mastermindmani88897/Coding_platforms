class Solution:
    def minCost(self, heights, cost):
        pairs = sorted(zip(heights, cost))
        
        total_weight = sum(cost)
        cumulative = 0
        target = 0
        
        for h, c in pairs:
            cumulative += c
            if cumulative * 2 >= total_weight:
                target = h
                break
        
        total_cost = 0
        for h, c in pairs:
            total_cost += abs(h - target) * c
        
        return total_cost
