class Solution:
    def minOperations(self, s: str) -> int:
        c1=0
        c2=0
        for i,ch in enumerate(s):
            if i%2==0:
                if ch!='0':
                    c1+=1
                if ch!='1':
                    c2+=1
            else:
                if ch!='1':
                    c1+=1
                if ch!='0':
                    c2+=1
        return min(c1,c2)