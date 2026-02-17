class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        mx=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    mx=max(mx,nums[i]^nums[j])
        return mx