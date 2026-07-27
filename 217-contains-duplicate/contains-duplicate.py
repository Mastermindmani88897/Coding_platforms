from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=Counter(nums)
        for key,val in l.items():
            if val>1:
                return True
        return False


      