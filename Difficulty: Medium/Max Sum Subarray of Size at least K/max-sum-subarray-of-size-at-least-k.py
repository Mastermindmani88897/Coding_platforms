class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        ans = -10**18
        min_prefix = 0

        for i in range(k, n + 1):
            min_prefix = min(min_prefix, prefix[i - k])
            ans = max(ans, prefix[i] - min_prefix)

        return ans