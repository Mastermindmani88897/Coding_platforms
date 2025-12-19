from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        li=[]
        li=Counter(nums)
        c=0
        for key,val in li.items():
            if val==1:
                c=c+key
        return c