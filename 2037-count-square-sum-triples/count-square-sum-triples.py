class Solution:
    def countTriples(self, n):
        if n <= 2:
            return 0
        s = set()
        for i in range(1, n + 1):
            s.add(i * i)
        c = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n + 1):
                need = i * i + j * j
                if need in s:
                    c += 1
        return c * 2
