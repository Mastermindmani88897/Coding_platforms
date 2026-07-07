class Solution:
    def largestArea(self, n, m, arr):
        rows = sorted([r for r, c in arr])
        cols = sorted([c for r, c in arr])

        max_row = 0
        prev = 0
        for r in rows:
            max_row = max(max_row, r - prev - 1)
            prev = r
        max_row = max(max_row, n - prev)

        max_col = 0
        prev = 0
        for c in cols:
            max_col = max(max_col, c - prev - 1)
            prev = c
        max_col = max(max_col, m - prev)

        return max_row * max_col