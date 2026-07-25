class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)

        pre = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )

        ans = -10**18

        for i in range(k, n + 1):
            for j in range(k, n + 1):
                s = (
                    pre[i][j]
                    - pre[i - k][j]
                    - pre[i][j - k]
                    + pre[i - k][j - k]
                )
                ans = max(ans, s)

        return ans