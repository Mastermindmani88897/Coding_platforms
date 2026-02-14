class Solution:
    def minTime(self, arr, k):
        def can_paint(max_time):
            painters = 1
            curr_sum = 0
            
            for length in arr:
                if curr_sum + length <= max_time:
                    curr_sum += length
                else:
                    painters += 1
                    curr_sum = length
                    
                    if painters > k:
                        return False
            return True
        
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_paint(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
