class Solution:
    def maxCircularSum(self, arr):
        total = sum(arr)
        
        max_kadane = cur_max = arr[0]
        min_kadane = cur_min = arr[0]
        
        for x in arr[1:]:
            cur_max = max(x, cur_max + x)
            max_kadane = max(max_kadane, cur_max)
            
            cur_min = min(x, cur_min + x)
            min_kadane = min(min_kadane, cur_min)
        
        if max_kadane < 0:
            return max_kadane
        
        return max(max_kadane, total - min_kadane)
