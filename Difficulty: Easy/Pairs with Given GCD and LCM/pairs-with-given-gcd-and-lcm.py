class Solution:
    def pairCount(self, x, y):
        if y % x != 0:
            return 0

        n = y // x
        ans = 0

        for a in range(1, int(n ** 0.5) + 1):
            if n % a == 0:
                b = n // a

                import math
                if math.gcd(a, b) == 1:
                    ans += 1 if a == b else 2

        return ans