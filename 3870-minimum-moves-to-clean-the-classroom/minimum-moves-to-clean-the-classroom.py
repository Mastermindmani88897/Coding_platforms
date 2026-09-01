from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None
        total = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = total
                    total += 1

        if total == 0:
            return 0

        full = (1 << total) - 1
        q = deque()
        q.append((start[0], start[1], 0, energy))
        visited = {(start[0], start[1], 0, energy)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = 0

        while q:
            for _ in range(len(q)):
                x, y, mask, e = q.popleft()

                if mask == full:
                    return moves

                if e == 0:
                    continue

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if classroom[nx][ny] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    if (nx, ny) in litter:
                        nmask |= 1 << litter[(nx, ny)]

                    if classroom[nx][ny] == 'R':
                        ne = energy

                    state = (nx, ny, nmask, ne)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1