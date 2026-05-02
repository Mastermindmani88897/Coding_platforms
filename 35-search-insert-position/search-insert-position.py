import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bisect.insort(nums,target)
        return bisect.bisect_left(nums,target)