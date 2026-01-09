class Solution:
    def countAtMostK(self, arr, k):
        freq={}
        l=0
        ans=0
        distinct=0
        for r in range(len(arr)):
            if arr[r] not in freq or freq[arr[r]]==0:
                distinct+=1
            freq[arr[r]]=freq.get(arr[r],0)+1
            while distinct>k:
                freq[arr[l]]-=1
                if freq[arr[l]]==0:
                    distinct-=1
                l+=1
            ans+=r-l+1
        return ans
