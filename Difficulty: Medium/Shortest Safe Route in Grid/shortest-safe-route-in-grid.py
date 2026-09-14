class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        from collections import deque

        n = len(mat)
        m = len(mat[0])

        unsafe = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    unsafe[i][j] = True
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            unsafe[ni][nj] = True

        q = deque()

        for i in range(n):
            if not unsafe[i][0]:
                q.append((i, 0, 1))
                unsafe[i][0] = True

        while q:
            r, c, dist = q.popleft()

            if c == m - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and not unsafe[nr][nc]:
                    unsafe[nr][nc] = True
                    q.append((nr, nc, dist + 1))

        return -1