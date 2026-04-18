class Solution:
    def maxOnes(self, arr):
        # code here
        ans=0
        ms=0
        c=0
        s=0
        for i in arr:
            if i==0:
                v=1
            else:
                v=-1
            s=max(v,v+s)
            ms=max(ms,s)
            if i==1:
                c+=1
        return c+ms