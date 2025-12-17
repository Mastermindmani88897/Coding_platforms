class Solution:
    def mergeOverlap(self, arr):
        arr.sort(key=lambda x: x[0])
        res = []
        for s, e in arr:
            if not res or res[-1][1] < s:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
