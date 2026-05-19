from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        
        if start == end:
            return 0
        
        dist = [-1] * 1000
        dist[start] = 0
        
        q = deque([start])
        
        while q:
            num = q.popleft()
            
            for x in arr:
                nxt = (num * x) % 1000
                
                if dist[nxt] == -1:
                    dist[nxt] = dist[num] + 1
                    
                    if nxt == end:
                        return dist[nxt]
                    
                    q.append(nxt)
        
        return -1