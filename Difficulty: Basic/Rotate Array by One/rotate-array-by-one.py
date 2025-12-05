class Solution:
    def rotate(self, arr):
        arr[:] = [arr[-1]] + arr[:-1]
        return arr
