from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        start_count = 1
        dist[0][start_count] = 0

        pq = [(0, 0, start_count)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, weight in adj[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                if next_count <= k:
                    new_cost = cost + weight

                    if new_cost < dist[v][next_count]:
                        dist[v][next_count] = new_cost
                        heapq.heappush(pq, (new_cost, v, next_count))

        return -1