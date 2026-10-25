class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds, it's not a closed island (touches the border)
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            # If it's water (1), it's part of the boundary/sea, return True (doesn't invalidate the island)
            if grid[r][c] == 1:
                return True
            
            # Mark the current land cell as visited by changing it to 1
            grid[r][c] = 1
            
            # Explore all 4 directions
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            
            # The island is closed only if all four directions are valid (closed)
            return left and right and up and down

        closed_islands_count = 0
        
        for r in range(rows):
            for c in range(cols):
                # If we find an unvisited land cell (0), run DFS to explore the island
                if grid[r][c] == 0:
                    if dfs(r, c):
                        closed_islands_count += 1
                        
        return closed_islands_count