class Solution:
    def levelSort(self, arr):
        ans = []
        i = 0
        level = 1
        n = len(arr)

        while i < n:
            cur = arr[i:min(i + level, n)]
            cur.sort()
            ans.append(cur)
            i += level
            level <<= 1

        return ans