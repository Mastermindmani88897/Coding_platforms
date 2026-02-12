class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def can_make(target):
            diff = [0] * (n + 1)
            curr_add = 0
            ops = 0
            
            for i in range(n):
                curr_add += diff[i]
                
                if arr[i] + curr_add < target:
                    need = target - (arr[i] + curr_add)
                    ops += need
                    if ops > k:
                        return False
                    
                    curr_add += need
                    if i + w < n:
                        diff[i + w] -= need
                        
            return True
        
        low = min(arr)
        high = low + k
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_make(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
