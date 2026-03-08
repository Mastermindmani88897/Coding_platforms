class Solution:
    def pythagoreanTriplet(self, arr):
        freq=[0]*1001
        for v in arr:
            freq[v]+=1
        for a in range(1,1001):
            if freq[a]==0: 
                continue
            for b in range(a,1001):
                if freq[b]==0: 
                    continue
                c2=a*a+b*b
                c=int(c2**0.5)
                if c*c!=c2 or c>1000 or freq[c]==0:
                    continue
                if a==b==c:
                    if freq[a]>=3: 
                        return True
                elif a==b:
                    if freq[a]>=2: 
                        return True
                elif b==c:
                    if freq[b]>=2: 
                        return True
                elif a==c:
                    if freq[a]>=2: 
                        return True
                else:
                    return True
        return False