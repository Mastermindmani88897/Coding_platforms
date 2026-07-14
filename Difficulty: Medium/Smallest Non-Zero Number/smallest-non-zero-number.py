class Solution:
    def find(self, arr):
        need = 0

        for x in reversed(arr):
            need = (need + x + 1) // 2

        return need