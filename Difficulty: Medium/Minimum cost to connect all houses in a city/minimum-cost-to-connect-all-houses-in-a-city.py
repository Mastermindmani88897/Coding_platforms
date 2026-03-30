import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]
        result = 0
        edges_used = 0
        
        while edges_used < n:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            
            visited[u] = True
            result += cost
            edges_used += 1
            
            x1, y1 = houses[u]
            
            for v in range(n):
                if not visited[v]:
                    x2, y2 = houses[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, v))
        
        return result