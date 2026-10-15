class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                a=len(set(nums[i:j]))
                s+=a*a
        return s