class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        li=list(set(nums))
        del nums[:]
        nums.extend(li)
        nums.sort()
        return len(nums)