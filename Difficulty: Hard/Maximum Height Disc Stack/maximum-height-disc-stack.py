class Solution:
    def maxStackHeight(self, r, h):
        discs = sorted(zip(r, h))
        m = 1000

        bit = [0] * (m + 1)

        def query(x):
            res = 0
            while x > 0:
                res = max(res, bit[x])
                x -= x & -x
            return res

        def update(x, val):
            while x <= m:
                bit[x] = max(bit[x], val)
                x += x & -x

        ans = 0
        i = 0
        n = len(discs)

        while i < n:
            j = i
            while j < n and discs[j][0] == discs[i][0]:
                j += 1

            updates = []

            for k in range(i, j):
                radius, height = discs[k]
                best = query(height - 1)
                curr = best + height
                updates.append((height, curr))
                ans = max(ans, curr)

            for height, curr in updates:
                update(height, curr)

            i = j

        return ans