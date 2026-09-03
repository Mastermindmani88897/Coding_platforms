class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = [x for x in nums1 if x % 2 == 1]
        even = [x for x in nums1 if x % 2 == 0]

        if not odd or not even:
            return True

        return min(odd) < min(even)