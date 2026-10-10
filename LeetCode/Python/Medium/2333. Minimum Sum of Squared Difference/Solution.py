class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                high = mid
            else:
                low = mid + 1

        limit = low
        operations = sum(max(0, d - limit) for d in diff)

        ans = sum(min(d, limit) ** 2 for d in diff)
        remaining = k - operations

        for d in diff:
            if d >= limit and remaining > 0:
                ans -= 2 * limit - 1
                remaining -= 1

        return ans