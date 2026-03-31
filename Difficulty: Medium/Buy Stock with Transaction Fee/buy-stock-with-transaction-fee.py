class Solution:
    def maxProfit(self, arr, k):
        hold = -arr[0]
        cash = 0
        
        for i in range(1, len(arr)):
            cash = max(cash, hold + arr[i] - k)
            hold = max(hold, cash - arr[i])
        
        return cash