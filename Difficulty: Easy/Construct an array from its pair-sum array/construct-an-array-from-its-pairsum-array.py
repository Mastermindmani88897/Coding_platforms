class Solution:
    def constructArr(self, arr):
        m = len(arr)
        if m == 1:
            return [1, arr[0] - 1]

        n = 0
        while n * (n - 1) // 2 < m:
            n += 1

        res = [0] * n
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2

        idx = 0
        for i in range(1, n):
            res[i] = arr[idx] - res[0]
            idx += 1

        return res
