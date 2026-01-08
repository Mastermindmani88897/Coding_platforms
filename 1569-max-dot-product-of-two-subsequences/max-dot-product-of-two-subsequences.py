class Solution:
    def maxDotProduct(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        dp=[[-10**18]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                v=nums1[i]*nums2[j]
                dp[i+1][j+1]=max(
                    v,
                    dp[i][j]+v,
                    dp[i][j+1],
                    dp[i+1][j]
                )
        return dp[n][m]
