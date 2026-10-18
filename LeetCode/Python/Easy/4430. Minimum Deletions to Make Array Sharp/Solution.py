class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletions = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                deletions += 1
            else:
                prev = nums[i]

        return deletions