class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pref=[0]
        for x in nums:
            pref.append(pref[-1]+x)
        best=[10**30]*k
        best[0]=0
        ans=-10**30
        for i in range(1,n+1):
            r=i%k
            ans=max(ans,pref[i]-best[r])
            best[r]=min(best[r],pref[i])
        return ans
