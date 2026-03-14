class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        s=0
        ps={0:1}
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in ps:
                c=c+ps[s-k]
            if s in ps:
                ps[s]+=1
            else:
                ps[s]=1
        return c