class Solution:
    def catchThieves(self, arr, k):
        p=[]
        t=[]
        for i,x in enumerate(arr):
            if x=='P':
                p.append(i)
            else:
                t.append(i)
        
        i=j=0
        ans=0
        while i<len(p) and j<len(t):
            if abs(p[i]-t[j])<=k:
                ans+=1
                i+=1
                j+=1
            elif t[j]<p[i]:
                j+=1
            else:
                i+=1
        return ans
