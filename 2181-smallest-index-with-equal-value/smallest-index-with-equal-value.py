class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        mn=101
        c=0
        for i in range(len(nums)):
            if nums[i]==i%10:
                mn=min(mn,i)
                c=c+1
        if c>=1:
            return mn
        else:
            return -1