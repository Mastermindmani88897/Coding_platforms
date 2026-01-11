class Solution:
    def minWindow(self, s1, s2):
        n=len(s1)
        m=len(s2)
        ans=""
        minlen=10**18
        
        i=0
        while i<n:
            if s1[i]!=s2[0]:
                i+=1
                continue
            
            j=i
            k=0
            while j<n and k<m:
                if s1[j]==s2[k]:
                    k+=1
                j+=1
            
            if k<m:
                break
            
            end=j-1
            k=m-1
            j=end
            while j>=i:
                if s1[j]==s2[k]:
                    k-=1
                if k<0:
                    break
                j-=1
            
            start=j
            if end-start+1<minlen:
                minlen=end-start+1
                ans=s1[start:end+1]
            
            i=start+1
        
        return ans
