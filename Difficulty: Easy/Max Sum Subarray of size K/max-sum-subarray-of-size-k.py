class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        s=sum(arr[:k])
        mx=s
        if k>=len(arr):
            return s
        for i in range(k,len(arr)):
            s=s+arr[i]-arr[i-k]
            if s>mx:
                mx=s
        return mx
            
        