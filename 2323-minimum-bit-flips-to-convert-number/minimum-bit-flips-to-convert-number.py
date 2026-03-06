class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        c=0
        while x!=0:
            x=x&(x-1)
            c=c+1
        return c