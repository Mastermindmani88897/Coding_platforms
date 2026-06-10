class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        stack = [(0, n - 1, float('-inf'), float('inf'))]

        while stack:
            l, r, low, high = stack.pop()

            if l > r:
                continue

            mid = (l + r) // 2

            if low < arr[mid] < high:
                ans += 1

            stack.append((l, mid - 1, low, min(high, arr[mid])))
            stack.append((mid + 1, r, max(low, arr[mid]), high))

        return ans