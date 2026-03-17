from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        l=Counter(nums)
        for i in range(len(nums)):
            if nums[i]%2==0 and l[nums[i]]==1:
                return nums[i]
        return -1