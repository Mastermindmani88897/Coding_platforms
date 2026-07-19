class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        incEnd = [0] * n
        decEnd = [0] * n

        incEnd[-1] = decEnd[-1] = n - 1

        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                incEnd[i] = incEnd[i + 1]
            else:
                incEnd[i] = i

            if arr[i] >= arr[i + 1]:
                decEnd[i] = decEnd[i + 1]
            else:
                decEnd[i] = i

        ans = []
        for l, r in queries:
            peak = incEnd[l]
            ans.append(decEnd[peak] >= r)

        return ans