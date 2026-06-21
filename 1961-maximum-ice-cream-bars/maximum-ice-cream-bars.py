class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in range(len(costs)):
            if coins>=costs[i]:
                coins=coins-costs[i]
                c=c+1
        return c
        
            