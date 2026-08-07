class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binary_search(arr, x)
        n = len(arr)

        left = index - 1
        right = index

        while (left >= 0 or right < n) and (right-left-1) < k:
            if left >= 0 and right < n:
                if abs(arr[left]-x) <= abs(arr[right]-x):
                    left -= 1
                else:
                    right += 1
            elif left >= 0:
                left -= 1
            elif right < n:
                right += 1

        return arr[left+1:right]

    def binary_search(self, arr, target):
        i, j = 0, len(arr) - 1
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i