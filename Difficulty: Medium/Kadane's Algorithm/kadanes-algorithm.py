class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        res=arr[0]
        mx=arr[0]
        for i in range(1,len(arr)):
            mx=max(mx+arr[i],arr[i])
            res=max(res,mx)
        return res
            