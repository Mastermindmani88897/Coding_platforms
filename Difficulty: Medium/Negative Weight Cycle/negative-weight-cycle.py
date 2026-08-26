class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        dist = [0] * V
    
        for _ in range(V):
            updated = False
    
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
    
            if not updated:
                return False
    
        return True