class Solution:
    def countSubstr(self, s, k):
        def atMost(k):
            freq={}
            l=0
            res=0
            distinct=0
            for r in range(len(s)):
                if freq.get(s[r],0)==0:
                    distinct+=1
                freq[s[r]]=freq.get(s[r],0)+1
                while distinct>k:
                    freq[s[l]]-=1
                    if freq[s[l]]==0:
                        distinct-=1
                    l+=1
                res+=r-l+1
            return res
        return atMost(k)-atMost(k-1)
