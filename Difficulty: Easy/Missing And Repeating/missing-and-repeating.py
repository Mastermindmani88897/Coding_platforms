class Solution:
    def findTwoElement(self, arr):
        n=len(arr)
        s1=n*(n+1)//2
        s2=sum(arr)
        s3=n*(n+1)*(2*n+1)//6
        s4=sum(x*x for x in arr)
        diff=s2-s1
        diff2=s4-s3
        dup=(diff2//diff+diff)//2
        miss=dup-diff
        return dup,miss
