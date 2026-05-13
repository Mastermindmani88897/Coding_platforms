class Solution:
    def findMotherVertex(self, V, edges):
        
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        candidate = -1
        
        def dfs(node):
            visited[node] = True
            
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
                candidate = i
        
        visited = [False] * V
        dfs(candidate)
        
        if not all(visited):
            return -1
        
        res = candidate
        
        for i in range(candidate):
            visited = [False] * V
            dfs_check = [False] * V
            
            def check(node):
                dfs_check[node] = True
                
                for nei in adj[node]:
                    if not dfs_check[nei]:
                        check(nei)
            
            check(i)
            
            if all(dfs_check):
                res = i
                break
        
        return res