class Solution:
    def finalElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(nums[0], nums[-1])
