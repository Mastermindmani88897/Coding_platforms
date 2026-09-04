class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
    
        if m == n:
            return sum(arr)
    
        curr = sum(arr[:m])
        ans = curr
    
        for i in range(m, n + m - 1):
            curr += arr[i % n] - arr[(i - m) % n]
            ans = max(ans, curr)
    
        return ans