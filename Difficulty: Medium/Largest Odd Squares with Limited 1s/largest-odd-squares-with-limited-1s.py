class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        n = len(mat)
        m = len(mat[0])

        pre = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )

        def get_sum(r1, c1, r2, c2):
            return (
                pre[r2 + 1][c2 + 1]
                - pre[r1][c2 + 1]
                - pre[r2 + 1][c1]
                + pre[r1][c1]
            )

        ans = []

        for r, c in queries:
            max_radius = min(r, c, n - 1 - r, m - 1 - c)

            if mat[r][c] > k:
                ans.append(-1)
                continue

            lo = 0
            hi = max_radius
            best = 0

            while lo <= hi:
                mid = (lo + hi) // 2

                ones = get_sum(
                    r - mid,
                    c - mid,
                    r + mid,
                    c + mid
                )

                if ones <= k:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1

            ans.append(2 * best + 1)

        return ans