from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        
        x = y = 0
        d = 0
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                for _ in range(cmd):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if (nx, ny) in obs:
                        break
                    
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist