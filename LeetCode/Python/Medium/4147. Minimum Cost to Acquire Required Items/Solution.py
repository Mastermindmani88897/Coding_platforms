class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Use type 3 (both) to satisfy the overlapping requirements min(need1, need2)
        common_need = min(need1, need2)
        cost_for_common = common_need * min(costBoth, cost1 + cost2)
        
        # Remaining requirement for type 1
        rem1 = need1 - common_need
        cost_for_rem1 = rem1 * min(costBoth, cost1)
        
        # Remaining requirement for type 2
        rem2 = need2 - common_need
        cost_for_rem2 = rem2 * min(costBoth, cost2)
        
        return cost_for_common + cost_for_rem1 + cost_for_rem2