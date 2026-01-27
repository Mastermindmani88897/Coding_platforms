class Solution:
    def isPrime(self, n):
        # code here
        if n<=1:
            return False
        bo=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                bo=False
        return bo