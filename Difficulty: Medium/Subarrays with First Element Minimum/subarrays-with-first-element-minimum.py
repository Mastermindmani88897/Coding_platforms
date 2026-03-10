class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        R = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                R[stack.pop()] = i
            stack.append(i)
        
       
        ans = 0
        for i in range(n):
            ans += (R[i] - i)
            
        return ans
