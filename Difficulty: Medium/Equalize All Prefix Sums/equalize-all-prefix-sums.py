class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
        
        ans = []
        
        for i in range(n):
            m = i // 2
            med = arr[m]
            
            left = med * (m + 1) - pref[m + 1]
            right = (pref[i + 1] - pref[m + 1]) - med * (i - m)
            
            ans.append(left + right)
        
        return ans