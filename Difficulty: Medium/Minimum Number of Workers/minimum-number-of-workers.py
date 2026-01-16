class Solution:
    def minMen(self, arr):
        n=len(arr)
        intervals=[]
        for i,x in enumerate(arr):
            if x!=-1:
                l=max(0,i-x)
                r=min(n-1,i+x)
                intervals.append((l,r))
        
        intervals.sort()
        
        ans=0
        i=0
        covered=0
        
        while covered<n:
            far=covered
            while i<len(intervals) and intervals[i][0]<=covered:
                far=max(far,intervals[i][1]+1)
                i+=1
            if far==covered:
                return -1
            ans+=1
            covered=far
        
        return ans
