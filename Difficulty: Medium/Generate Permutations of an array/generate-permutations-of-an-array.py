class Solution:
    def permuteDist(self, arr):
        res = []
        used = [False] * len(arr)

        def backtrack(path):
            if len(path) == len(arr):
                res.append(path[:])
                return

            for i in range(len(arr)):
                if not used[i]:
                    used[i] = True
                    path.append(arr[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res
