class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o=0
        e=0
        for i in range(1,2*n+1,1):
            if i%2==0:
                e+=i
            else:
                o+=i
        return math.gcd(e,o)