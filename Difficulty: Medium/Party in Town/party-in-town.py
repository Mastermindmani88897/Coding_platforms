class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        from collections import deque

        n = len(adj)

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])

            farthest = start

            while q:
                u = q.popleft()

                if dist[u] > dist[farthest]:
                    farthest = u

                for v in adj[u]:
                    v -= 1
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)

            return farthest, dist[farthest]

        a, _ = bfs(0)
        b, diameter = bfs(a)

        return (diameter + 1) // 2