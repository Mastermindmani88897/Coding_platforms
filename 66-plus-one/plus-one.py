class Solution:
    def plusOne(self, arr):
        for i in range(len(arr) - 1, -1, -1):
            arr[i] += 1
            if arr[i] == 10:
                arr[i] = 0
            else:
                return arr

        res = [0] * (len(arr) + 1)
        res[0] = 1
        for i in range(len(arr)):
            res[i + 1] = arr[i]
        return res
