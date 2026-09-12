class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        mx = [None] * (k + 1)
        mn = [None] * (k + 1)

        mx[0] = mn[0] = 1

        for x in arr:
            for j in range(k, 0, -1):
                if mx[j - 1] is not None:
                    a = mx[j - 1] * x
                    b = mn[j - 1] * x

                    if mx[j] is None:
                        mx[j] = max(a, b)
                        mn[j] = min(a, b)
                    else:
                        mx[j] = max(mx[j], a, b)
                        mn[j] = min(mn[j], a, b)

        return mx[k]