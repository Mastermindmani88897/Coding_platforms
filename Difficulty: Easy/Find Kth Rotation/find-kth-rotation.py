class Solution:
    def findKRotation(self, arr):
        low, high = 0, len(arr) - 1

        while low <= high:
            if arr[low] <= arr[high]:
                return low

            mid = (low + high) // 2
            prev = (mid - 1 + len(arr)) % len(arr)
            nxt = (mid + 1) % len(arr)

            if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
                return mid

            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
