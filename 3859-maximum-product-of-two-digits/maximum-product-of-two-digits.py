class Solution:
    def maxProduct(self, n: int) -> int:
        li=[]
        r1=0
        n1=0
        while(n!=0):
            n1=n%10
            li.append(n1)
            r1=r1*10+n1
            n=n//10
        li.sort()
        return li[len(li)-2]*li[len(li)-1]
            