class Solution:
    def shortestDist(self, mat):
        n = len(mat)

        if mat[0][0] == 0:
            return [[-1]]

        path = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        def dfs(i, j):
            if i == n - 1 and j == n - 1:
                path[i][j] = 1
                return True

            if visited[i][j] or mat[i][j] == 0:
                return False

            visited[i][j] = True
            path[i][j] = 1

            jump = mat[i][j]

            for k in range(1, jump + 1):
                nj = j + k
                if nj < n and dfs(i, nj):
                    return True

                ni = i + k
                if ni < n and dfs(ni, j):
                    return True

            path[i][j] = 0
            return False

        if dfs(0, 0):
            return path

        return [[-1]]