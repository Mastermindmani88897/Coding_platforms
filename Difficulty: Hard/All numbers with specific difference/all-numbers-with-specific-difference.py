class Solution:
    def getCount(self, n, d):
        
        def digit_sum(x):
            return sum(int(c) for c in str(x))
        
        left, right = 1, n
        ans = n + 1  # default if no valid x found
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid - digit_sum(mid) >= d:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if ans == n + 1:
            return 0
        
        return n - ans + 1
