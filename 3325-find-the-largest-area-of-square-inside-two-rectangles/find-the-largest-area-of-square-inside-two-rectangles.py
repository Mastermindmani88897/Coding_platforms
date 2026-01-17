class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        ans = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                lx = max(bottomLeft[i][0], bottomLeft[j][0])
                rx = min(topRight[i][0], topRight[j][0])
                ly = max(bottomLeft[i][1], bottomLeft[j][1])
                uy = min(topRight[i][1], topRight[j][1])

                if lx < rx and ly < uy:
                    side = min(rx - lx, uy - ly)
                    ans = max(ans, side * side)

        return ans