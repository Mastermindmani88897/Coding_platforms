from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        # build graph
        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
        
        q = deque()
        
        # push nodes with indegree 0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count == n