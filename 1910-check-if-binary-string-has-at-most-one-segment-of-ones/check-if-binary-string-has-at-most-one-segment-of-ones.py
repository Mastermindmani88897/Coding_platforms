class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c=0
        c1=0
        if s=='1':
            return True
        for i in range(0,len(s)):
            if s[i]=='1':
                c+=1
            else: 
                c1+= c if c==0 else 1
                c=0
        c1+= c if c==0 else 1
        return c1<=1