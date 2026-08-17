from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        N = n * n
        jump = {}

        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]

        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        dist = [-1] * (N + 1)
        dist[1] = 0

        q = deque([1])

        while q:
            pos = q.popleft()

            if pos == N:
                return dist[pos]

            for dice in range(1, 7):
                nxt = pos + dice

                if nxt > N:
                    continue

                if nxt in jump:
                    nxt = jump[nxt]

                if dist[nxt] == -1:
                    dist[nxt] = dist[pos] + 1
                    q.append(nxt)

        return -1