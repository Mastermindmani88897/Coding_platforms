class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)

        dp = mat[0][:]

        for i in range(1, n):
            best1 = best2 = -1
            idx1 = -1

            for j in range(n):
                if dp[j] > best1:
                    best2 = best1
                    best1 = dp[j]
                    idx1 = j
                elif dp[j] > best2:
                    best2 = dp[j]

            new = [0] * n

            for j in range(n):
                if j != idx1:
                    new[j] = mat[i][j] + best1
                else:
                    new[j] = mat[i][j] + best2

            dp = new

        return max(dp)