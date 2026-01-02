from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        li=Counter(nums)
        for key,val in li.items():
            if val%len(nums)//2:
                return key