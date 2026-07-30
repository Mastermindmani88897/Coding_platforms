class Solution:
    def maxSubsetXOR(self, arr):
        n = len(arr)
        index = 0

        for bit in range(31, -1, -1):
            pivot = index
            while pivot < n and ((arr[pivot] >> bit) & 1) == 0:
                pivot += 1

            if pivot == n:
                continue

            arr[index], arr[pivot] = arr[pivot], arr[index]

            for i in range(n):
                if i != index and ((arr[i] >> bit) & 1):
                    arr[i] ^= arr[index]

            index += 1

        ans = 0
        for x in arr:
            ans = max(ans, ans ^ x)

        return ans