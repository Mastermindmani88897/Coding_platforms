class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = 0
        pairs = {}

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                base += 1
            else:
                a, b = nums[i - 1], nums[i]
                if a > b:
                    a, b = b, a
                pairs[(a, b)] = pairs.get((a, b), 0) + 1

        return base + max(pairs.values(), default=0)