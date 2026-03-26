class Solution:
    def countPaths(self, V, edges):
        import heapq
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node]:
                continue
            
            for nei, wt in graph[node]:
                new_dist = d + wt
                
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                
                elif new_dist == dist[nei]:
                    ways[nei] += ways[node]
        
        return ways[V - 1]