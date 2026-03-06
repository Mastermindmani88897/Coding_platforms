class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        for i in range(len(nums)):
            x=x^nums[i]
        x=x^k
        c=0
        while x!=0:
            x=x&(x-1)
            c=c+1
        return c