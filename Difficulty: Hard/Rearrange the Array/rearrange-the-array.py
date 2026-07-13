class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7
        n = len(b)

        vis = [False] * n
        cycles = []

        for i in range(n):
            if not vis[i]:
                cnt = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = b[j] - 1
                    cnt += 1
                cycles.append(cnt)

        limit = n
        spf = list(range(limit + 1))
        for i in range(2, int(limit ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        mp = {}

        for x in cycles:
            while x > 1:
                p = spf[x]
                c = 0
                while x % p == 0:
                    x //= p
                    c += 1
                if c > mp.get(p, 0):
                    mp[p] = c

        ans = 1
        for p, e in mp.items():
            ans = (ans * pow(p, e, MOD)) % MOD

        return ans