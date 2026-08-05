class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        def count_le(limit):
            if limit < 0:
                return 0
            left = 0
            s = 0
            ans = 0
            for right in range(len(arr)):
                s += arr[right]
                while s > limit:
                    s -= arr[left]
                    left += 1
                ans += right - left + 1
            return ans

        return count_le(r) - count_le(l - 1)