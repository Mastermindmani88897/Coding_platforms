class Solution:
    def minSwaps(self, arr):
        k = sum(arr)
        
        if k == 0:
            return -1
        
        curr = sum(arr[:k])
        max_ones = curr
        
        for i in range(k, len(arr)):
            curr += arr[i]
            curr -= arr[i - k]
            max_ones = max(max_ones, curr)
        
        return k - max_ones