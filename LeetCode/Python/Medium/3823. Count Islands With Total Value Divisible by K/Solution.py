class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    # BFS to find total value of the island
                    total_value = 0
                    queue = [(r, c)]
                    # Temporarily store and zero out
                    val = grid[r][c]
                    grid[r][c] = 0
                    total_value += val
                    
                    head = 0
                    while head < len(queue):
                        curr_r, curr_c = queue[head]
                        head += 1
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                total_value += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                                
                    if total_value % k == 0:
                        island_count += 1
                        
        return island_count